from mcp_types import Prompt

from agents import movie_agent
from fastapi import FastAPI
from setup_db import query_duckdb

app = FastAPI()

@app.get("/movies")
async def read_movies(genre: str | None = None):
    if genre:
        sql = "SELECT * FROM movies WHERE genre = ?;"
        params = (genre)
    else:
        sql = "SELECT * FROM movies;"
        params = None
    movies = query_duckdb(sql, parameters=params)
    return movies.to_dict(orient="records")

@app.post("/movie")
async def create_movie(query: Prompt):
    result = await movie_agent.run(query)
    movie = result.output
    
    query_duckdb(
        "INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?)",
        parameters=(movie.title, movie.year, movie.genre, movie.rating, movie.director, movie.summary)
    )
    
    return movie
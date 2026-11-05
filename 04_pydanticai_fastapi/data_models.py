from pydantic import BaseModel, Field
from typing import Literal

class Movie(BaseModel):
    title: str = Field (description= "Movie title, if possible taken from IMDB or Rotten Tomatoes")
    year: int = Field(description= "Year of release, if possible taken from IMDB or Rotten Tomatoes", gt=1800, le=2100)
    genre: str = Field(description= "Movie genre, most fitting. Taken from IMDB or Rotten Tomatoes if possible")
    rating: float = Field(description= "Movie rating on a scale of 0 to 10, if possible taken from IMDB or Rotten Tomatoes", gt=0, le=10, precision=1) # Limit float 1 decimal places
    director: str = Field(description= "Movie director, if possible taken from IMDB or Rotten Tomatoes")
    summary: str = Field(description= "A brief summary of the movie plot")
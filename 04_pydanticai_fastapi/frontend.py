import streamlit as st
import requests
from fastapi import FastAPI

url = "http://localhost:8000/movies?genre={genre}"


def layout():
    st.markdown("# Cool Movies")

    movie_string = st.text_input("Give a statement and it will give backa movie")

    if movie_string:
        movie = requests.post("http://127.0.0.1:8000/movie", json={"prompt": movie_string}).json()
        st.write(movie)

    genre = st.selectbox(
        "Choose genre", options=["all","action", "comedy", "cartoon", "adventure", "romance"]
    )

    movies = requests.get(f"http://127.0.0.1:8000/movies?genre={genre}").json()

    st.dataframe(movies)


if __name__ == "__main__":
    layout()
from django.urls import path
from apps.movie.views import MovieDetail, SearchMovie, MovieGenreList


movie_pattern = [
    path("", SearchMovie.as_view(), name="search"),
    path("<int:movie_id>", MovieDetail.as_view(), name="movie-detail"),
    path("genre", MovieGenreList.as_view(), name="genre"),
]

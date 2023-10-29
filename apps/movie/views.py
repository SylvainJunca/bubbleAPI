from django.contrib.admin.utils import lookup_field
from rest_framework import generics
from rest_framework.views import APIView
from apps.movie.models import Movie
from rest_framework.response import Response
from apps.core.clients.tmdb import TMDBClient
from apps.movie.services import MovieService


class SearchMovie(APIView):
    def get(self, request):
        search = request.query_params["search"]
        tmdb_client = TMDBClient()
        response = tmdb_client.search(query=search)
        return Response(data=response)


class MovieDetail(APIView):
    def get(self, request, movie_id=None):
        movie = MovieService.get_movie(movie_id=movie_id)
        return Response(data=movie.data)


class MovieGenreList(APIView):
    def get(self, request, movie_id=None):
        tmdb_client = TMDBClient()
        response = tmdb_client.get_genre_list()
        return Response(data=response)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.core.clients.tmdb import TMDBClient


class SearchMovie(APIView):
    def get(self, request):
        search = request.query_params["search"]
        tmdb_client = TMDBClient()
        response = tmdb_client.search(query=search)
        return Response(data=response)


class MovieDetail(APIView):
    def get(self, request, movie_id=None):
        tmdb_client = TMDBClient()
        response = tmdb_client.get_movie_details(movie_id=movie_id)
        return Response(data=response)


class MovieGenreList(APIView):
    def get(self, request, movie_id=None):
        tmdb_client = TMDBClient()
        response = tmdb_client.get_genre_list()
        return Response(data=response)

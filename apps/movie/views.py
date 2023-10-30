from rest_framework.views import APIView
from rest_framework.response import Response
from apps.core.clients.tmdb import TMDBClient
from apps.movie.serializers import MovieDetailSerializer, MovieDetailValidator
from apps.movie.services import MovieServices


class SearchMovie(APIView):
    def get(self, request):
        search = request.query_params["search"]
        tmdb_client = TMDBClient()
        response = tmdb_client.search(query=search)
        return Response(data=response)


class MovieDetail(APIView):
    def get(self, request, movie_id=None):
        validator = MovieDetailValidator(data={"tmdb_id": movie_id})
        validator.is_valid()
        movie = MovieServices.get_movie(movie_id=movie_id)
        serializer = MovieDetailSerializer(movie)
        return Response(data=serializer.data)


class MovieGenreList(APIView):
    def get(self):
        tmdb_client = TMDBClient()
        response = tmdb_client.get_genre_list()
        return Response(data=response)

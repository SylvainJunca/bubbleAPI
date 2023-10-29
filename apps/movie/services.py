from django.http import Http404
from rest_framework import status
from apps.movie.serializers import MovieDetailSerializer
from apps.movie.models import Movie
from apps.core.clients.tmdb import TMDBClient
from requests.exceptions import HTTPError


class MovieServices:
    @staticmethod
    def get_movie(movie_id) -> Movie:
        try:
            movie = Movie.objects.get(tmdb_id=movie_id)
            return movie
        except Movie.DoesNotExist:
            tmdb_client = TMDBClient()
            response_movie = tmdb_client.get_movie_details(movie_id=movie_id)
            if response_movie.status_code == status.HTTP_200_OK:
                data = response_movie.json()
                new_movie = MovieDetailSerializer(
                    data={
                        "title": data["title"],
                        "tmdb_id": data["id"],
                        "metadata": data,
                    }
                )
                new_movie.is_valid()
                new_movie.save()
                return new_movie.instance
            else:
                raise Http404

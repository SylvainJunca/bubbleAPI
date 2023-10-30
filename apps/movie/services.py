from apps.movie.serializers import MovieDetailSerializer
from apps.movie.models import Movie
from apps.core.clients.tmdb import TMDBClient


class MovieServices:
    @staticmethod
    def get_movie(movie_id) -> Movie:
        try:
            movie = Movie.objects.get(tmdb_id=movie_id)
            return movie
        except Movie.DoesNotExist:
            tmdb_client = TMDBClient()
            response_movie = tmdb_client.get_movie_details(movie_id=movie_id)

            new_movie = MovieDetailSerializer(
                data={
                    "title": response_movie["title"],
                    "tmdb_id": response_movie["id"],
                    "metadata": response_movie,
                }
            )
            new_movie.is_valid()
            new_movie.save()
            return new_movie.instance

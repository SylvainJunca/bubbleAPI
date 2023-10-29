from apps.movie.serializers import MovieDetailSerializer
from apps.movie.models import Movie
from apps.core.clients.tmdb import TMDBClient


class MovieService:
    @staticmethod
    def get_movie(movie_id):
        try:
            movie = Movie.objects.get(tmdb_id=movie_id)
        except Movie.DoesNotExist:
            tmdb_client = TMDBClient()
            response_movie = tmdb_client.get_movie_details(movie_id=movie_id)
            if response_movie:
                new_movie = MovieDetailSerializer(
                    data={
                        "title": response_movie["title"],
                        "tmdb_id": response_movie["id"],
                        "metadata": response_movie,
                    }
                )
                new_movie.is_valid()
                new_movie.save()
                return new_movie
        return MovieDetailSerializer(movie)

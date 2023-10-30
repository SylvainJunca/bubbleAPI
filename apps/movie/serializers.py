from rest_framework import serializers
from apps.movie.models import Movie


class MovieDetailValidator(serializers.Serializer):
    tmdb_id = serializers.IntegerField(required=True)


class MovieDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    tmdb_id = serializers.IntegerField(required=True)
    metadata = serializers.JSONField(required=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "tmdb_id", "metadata"]

from rest_framework import serializers
from .models import Opinion


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = [
            "id",
            "user",
            "movie",
            "watched",
            "rewatch",
            "anticipation_rating",
            "rating",
            "favorite",
            "comment",
        ]

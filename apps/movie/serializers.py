from rest_framework import serializers


class MovieSearchResultSerializer(serializers.Serializer):
    page = serializers.In
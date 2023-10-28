from rest_framework import serializers
from apps.bubble.models import Bubble, BubbleUser
from apps.user.serializers import UserSerializer


class BubbleUserSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = BubbleUser
        fields = ["id", "user"]


class BubbleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3, max_length=32)
    owner = UserSerializer()

    class Meta:
        model = Bubble
        fields = ["id", "name", "owner"]

from rest_framework import generics
from apps.user.models import User
from apps.user.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.public()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.public()
    serializer_class = UserSerializer

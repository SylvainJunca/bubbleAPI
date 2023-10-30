from rest_framework import generics
from apps.Bubble.models import Bubble
from apps.Bubble.serializers import BubbleSerializer


class BubbleListView(generics.ListAPIView):
    queryset = Bubble.objects.all()
    serializer_class = BubbleSerializer


class BubbleDetailView(generics.RetrieveAPIView):
    queryset = Bubble.objects.all()
    serializer_class = BubbleSerializer


class BubbleCreateView(generics.CreateAPIView):
    queryset = Bubble.objects.all()
    serializer_class = BubbleSerializer

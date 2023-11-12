from rest_framework import viewsets
from .models import Opinion
from .serializers import OpinionSerializer


class OpinionViewSet(viewsets.ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer

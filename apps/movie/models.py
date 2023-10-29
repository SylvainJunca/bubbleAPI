from django.db import models
from apps.shared.models import UUIDModel, TimestampModel


class Movie(UUIDModel, TimestampModel):
    title = models.CharField(max_length=256)
    tmdb_id = models.IntegerField()
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "movies"

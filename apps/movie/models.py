from django.db import models
from apps.shared.models import UUIDModel, TimestampModel


class Movie(UUIDModel, TimestampModel):
    original_title = models.CharField(max_length=64)
    tmdb_id = models.IntegerField()
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = "movies"

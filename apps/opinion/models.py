from django.db import models
from apps.user.models import User
from apps.movie.models import Movie
from apps.shared.models import UUIDModel, TimestampModel
from apps.opinion.value_objects import AnticipationRatingChoices, RatingChoices


class Opinion(UUIDModel, TimestampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="opinions")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="opinions")
    watched = models.BooleanField(default=False)
    rewatch = models.BooleanField(default=False)
    anticipation_rating = models.IntegerField(
        choices=AnticipationRatingChoices.choices,
        default=AnticipationRatingChoices.OKAY,
    )
    rating = models.IntegerField(
        choices=RatingChoices.choices, default=RatingChoices.NOT_RATED
    )
    favorite = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.watched and self.rating != RatingChoices.NOT_RATED:
            raise ValueError("Cannot rate a movie that has not been watched")
        super().save(*args, **kwargs)

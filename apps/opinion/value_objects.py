from django.db import models


class AnticipationRatingChoices(models.IntegerChoices):
    NOPE = 10
    OKAY = 20
    GOOD = 30


class RatingChoices(models.IntegerChoices):
    NOT_RATED = 0
    NOPE = 10
    OKAY = 20
    GOOD = 30

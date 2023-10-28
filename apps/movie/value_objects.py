from django.db import models


class Rating(models.IntegerChoices):
    NO = 10
    MAYBE = 20
    YES = 30

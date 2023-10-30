from django.db import models
from apps.shared.models import UUIDModel, TimestampModel
from django.core.validators import MinLengthValidator, MaxLengthValidator
from apps.user.models import User


class Bubble(UUIDModel, TimestampModel):
    name = models.CharField(
        "name",
        max_length=32,
        validators=[MinLengthValidator(3), MaxLengthValidator(32)],
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="bubbles"
    )

    class Meta:
        db_table = "bubbles"


class BubbleUser(UUIDModel, TimestampModel):
    bubble = models.ForeignKey(
        Bubble, on_delete=models.CASCADE, null=True, related_name="bubble_users"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="bubble_users"
    )

    class Meta:
        db_table = "bubble_users"

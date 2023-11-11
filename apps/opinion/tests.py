from django.core.management import call_command
from apps.movie.models import Movie
from apps.opinion.models import Opinion
from apps.user.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from apps.opinion.value_objects import RatingChoices, AnticipationRatingChoices
from django.urls import reverse


class OpinionTests(APITestCase):
    def setUp(self) -> None:
        call_command("loaddata", ["users", "movies", "opinions"])
        self.existing_user = User.objects.get(id=1)
        self.existing_movie = Movie.objects.get(id=1)
        self.existing_opinion = Opinion.objects.get(id=1)
        self.endpoint = "/opinions/"

        return super().setUp()

    def test_create_opinion(self):
        data = {
            "user": self.existing_user.id,
            "movie": 1,
        }
        response = self.client.post(self.endpoint, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_opinion(self):
        response = self.client.get(f"{self.endpoint}{self.existing_opinion.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_opinion(self):
        updated_data = {"watched": True}
        response = self.client.patch(
            f"{self.endpoint}{self.existing_opinion.id}",
            updated_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_opinion(self):
        response = self.client.delete(f"{self.endpoint}{self.existing_opinion.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_invalid_opinion_with_rating_without_watch(self):
        invalid_data = {
            "user": self.existing_user.id,
            "movie": 1,
            "rating": RatingChoices.GOOD,
        }
        with self.assertRaises(ValueError):
            response = self.client.post(self.endpoint, invalid_data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_opinion(self):
        invalid_data = {"rating": 999}
        response = self.client.patch(
            f"{self.endpoint}{self.existing_opinion.id}", invalid_data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_non_existing_opinion(self):
        response = self.client.delete(f"{self.endpoint}99999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_rate_existing_unwatched_movie(self):
        invalid_data = {"rating": RatingChoices.GOOD}
        with self.assertRaises(ValueError):
            response = self.client.patch(
                f"{self.endpoint}{self.existing_opinion.id}", invalid_data
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

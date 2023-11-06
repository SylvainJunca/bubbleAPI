from django.core.management import call_command
from apps.user.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class UserTests(APITestCase):
    def setUp(self) -> None:
        call_command("loaddata", "users")
        self.existing_user = User.objects.get(id=1)

        return super().setUp()

    def test_create_user_successfully(self):
        data = {"username": "test", "email": "test@email.test", "password": "password"}
        response = self.client.post("/users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_without_username(self):
        data = {"email": "email@email.test", "password": "password"}
        response = self.client.post("/users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_email(self):
        data = {"username": "test", "password": "password"}
        response = self.client.post("/users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_password(self):
        data = {"username": "test", "email": "test@email.test"}
        response = self.client.post("/users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_existing_username(self):
        data = {"username": "test", "email": "test2@email.test", "password": "password"}
        self.client.post("/users/", data=data)
        response = self.client.post("/users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_existing_email(self):
        data = {"username": "test2", "email": "test@email.test", "password": "password"}
        self.client.post("/users/", data=data)
        response = self.client.post("/users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user(self):
        response = self.client.get(f"/users/{self.existing_user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.existing_user.username)

    def test_update_user(self):
        data = {"username": "new_username"}
        response = self.client.patch(f"/users/{self.existing_user.id}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "new_username")

    def test_delete_user(self):
        response = self.client.delete(f"/users/{self.existing_user.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

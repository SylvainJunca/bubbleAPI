from unittest import TestCase
from unittest.mock import patch

from apps.core.clients.tmdb import requests, TMDBClient


class TestTMDBClient(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @patch.object(requests, "get")
    def test_class_can_be(self, mock_get):
        print("#########")
        self.assertEqual(True, True)

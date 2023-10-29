from unittest.mock import patch
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from apps.movie.views import TMDBClient, MovieServices
from apps.core.tests.tests_tmdb_client import MockedTMDBClient

# Create your tests here.


class MovieTests(APITestCase):
    endpoint = "/movie/"
    existing_bubble_id = 12

    mock_tmdb_api_search_response = {"status": "success", "results": []}

    # mock_tmdb_api_detail_response = {"id" : }

    def setUp(self) -> None:
        return super().setUp()

    @patch.object(TMDBClient, "search")
    def test_search_movie_successfully(self, mock_tmdb_client):
        print(mock_tmdb_client is TMDBClient.search)
        # print(mock_tmdb_client)
        mock_tmdb_client.return_value = {
            "count": 1,
            "results": [{"id": "movie_1"}],
        }

        response = self.client.get(self.endpoint + "?search/")
        assert mock_tmdb_client.called_once()
        # mock_tmdb_client.assert_called_with("hello")
        print(mock_tmdb_client)
        # mock_tmdb_client.assert_called_with("hello")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch.object(MovieServices, "get_movie")
    def test_get_movie_successfully(self, mock_get_movie):
        mock_get_movie.return_value = {
            "id": "some_id",
            "tmdb_id": self.existing_bubble_id,
            "title": "title",
            "metadata": {},
        }
        response = self.client.get(self.endpoint + str(self.existing_bubble_id))

        assert mock_get_movie.called_once()
        mock_get_movie.assert_called_with(movie_id=self.existing_bubble_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

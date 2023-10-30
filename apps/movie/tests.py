from unittest.mock import patch
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase
from apps.movie.views import TMDBClient, MovieServices
from apps.core.tests.tests_tmdb_client import MockedTMDBClient


class MovieTests(APITestCase):
    endpoint = "/movie/"
    existing_bubble_id = 12

    mock_tmdb_api_search_response = {"status": "success", "results": []}

    # mock_tmdb_api_detail_response = {"id" : }

    def setUp(self) -> None:
        return super().setUp()

    @patch.object(TMDBClient, "search")
    def test_search_movie_successfully(self, mock_search):
        query = "kill bill"
        expected_result = {
            "count": 1,
            "results": [{"id": "movie_1"}],
        }
        mock_search.return_value = expected_result

        response = self.client.get(self.endpoint + "?search=" + query)
        assert mock_search.called_once()
        mock_search.assert_called_with(query=query)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_result)

    @patch.object(MovieServices, "get_movie")
    def test_get_movie_successfully(self, mock_get_movie):
        expected_result = {
            "id": "some_id",
            "tmdb_id": self.existing_bubble_id,
            "title": "title",
            "metadata": {},
        }
        mock_get_movie.return_value = expected_result
        response = self.client.get(self.endpoint + str(self.existing_bubble_id))

        assert mock_get_movie.called_once()
        mock_get_movie.assert_called_with(movie_id=self.existing_bubble_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_result)

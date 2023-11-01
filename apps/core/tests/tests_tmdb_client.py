from unittest import TestCase
from rest_framework.exceptions import ErrorDetail, NotFound
from apps.core.clients.tmdb import TMDBClient, requests
from unittest import mock
import os


class TestTMDBClient(TestCase):
    def _mock_response(
        self, status=200, content="CONTENT", json_data=None, raise_for_status=None
    ):
        mock_resp = mock.Mock()
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.text = raise_for_status
            mock_resp.json = mock.Mock(
                return_value=ErrorDetail(string=raise_for_status, code="404")
            )
            mock_resp.raise_for_status.side_effect = requests.HTTPError(
                raise_for_status, response=mock_resp
            )
        mock_resp.status_code = status
        mock_resp.content = content
        if json_data:
            mock_resp.json = mock.Mock(return_value=json_data)
        return mock_resp

    def test__create_headers(self):
        expected_result = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + os.environ.get("TMDB_TOKEN"),
        }
        tmdb_client = TMDBClient()
        self.assertEqual(tmdb_client._TMDBClient__create_headers(), expected_result)

    @mock.patch("requests.get")
    @mock.patch.object(TMDBClient, "_TMDBClient__create_headers")
    def test_search_returns_result_successfully(self, mock_create_headers, mock_get):
        expected_result = {
            "count": 1,
            "results": [{"id": "movie_1"}],
        }
        headers = "headers"
        mock_create_headers.return_value = headers
        mock_response = self._mock_response(json_data=expected_result)
        mock_get.return_value = mock_response

        query = "la vie en rose"
        tmdb_client = TMDBClient()
        result = tmdb_client.search(query)

        mock_get.assert_called_with(
            tmdb_client.root_url + "search/movie",
            params={"query": query},
            headers=headers,
        )
        mock_response.raise_for_status.called_once()
        self.assertEqual(result, expected_result)

    @mock.patch("requests.get")
    @mock.patch.object(TMDBClient, "_TMDBClient__create_headers")
    def test_search_when_get_request_fails(self, mock_create_headers, mock_get):
        expected_result = {}
        expected_result["text"] = "dsgdsgdfd"
        headers = "headers"
        mock_create_headers.return_value = headers
        mock_response = self._mock_response(
            json_data={"error": "error"}, status=404, raise_for_status="boom kaboom"
        )
        mock_get.return_value = mock_response

        query = "la vie en rose"
        tmdb_client = TMDBClient()
        with self.assertRaises(NotFound):
            tmdb_client.search(query)

    @mock.patch("requests.get")
    @mock.patch.object(TMDBClient, "_TMDBClient__create_headers")
    def test_detail_returns_result_successfully(self, mock_create_headers, mock_get):
        movie_id = 12
        expected_result = {
            "id": "some_id",
            "tmdb_id": movie_id,
            "title": "title",
            "metadata": {},
        }
        headers = "headers"
        mock_create_headers.return_value = headers
        mock_response = self._mock_response(json_data=expected_result)
        mock_get.return_value = mock_response

        tmdb_client = TMDBClient()

        result = tmdb_client.get_movie_details(movie_id)

        mock_get.assert_called_with(
            tmdb_client.root_url + "movie/" + str(movie_id),
            headers=headers,
        )
        mock_response.raise_for_status.called_once()
        self.assertEqual(result, expected_result)

    @mock.patch("requests.get")
    @mock.patch.object(TMDBClient, "_TMDBClient__create_headers")
    def test_get_movie_details_when_get_request_fails(
        self, mock_create_headers, mock_get
    ):
        movie_id = 12
        expected_result = {}
        expected_result["text"] = "dsgdsgdfd"
        headers = "headers"
        mock_create_headers.return_value = headers
        mock_response = self._mock_response(
            json_data={"error": "error"}, status=404, raise_for_status="boom kaboom"
        )
        mock_get.return_value = mock_response

        tmdb_client = TMDBClient()
        with self.assertRaises(NotFound):
            tmdb_client.get_movie_details(movie_id)

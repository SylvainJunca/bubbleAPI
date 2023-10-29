import requests
from requests.exceptions import HTTPError, RequestException
import os
import logging
from rest_framework import status

from rest_framework.response import Response


class TMDBClient:
    def __init__(self) -> None:
        self.root_url = "https://api.themoviedb.org/3/"
        self.bearer_token = os.environ.get("OMDB_TOKEN")

    def search(self, query):
        try:
            response = requests.get(
                self.root_url + "search/movie",
                params={"query": query},
                headers=self.__create_headers(),
            )
            response.raise_for_status()
            return response
        except (
            requests.exceptions.RequestException,
            requests.exceptions.HTTPError,
        ) as e:
            logging.error(
                f"TMDB search error - search {query} - response {e.response.text}"
            )

    def get_movie_details(self, movie_id: int):
        try:
            response = requests.get(
                self.root_url + "movie/" + str(movie_id),
                headers=self.__create_headers(),
            )
            response.raise_for_status()
            return response
        except (
            RequestException,
            HTTPError,
        ) as e:
            logging.error(
                f"TMDB search error - search tmdb_id {movie_id} - response {e.response.text}"
            )
            return Response({e.response.text}, status=status.HTTP_418_IM_A_TEAPOT)

    def get_genre_list(self, language="en"):
        response = requests.get(
            self.root_url + "genre/movie/list?language=" + language,
            headers=self.__create_headers(),
        )
        return response.json()

    def __create_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.bearer_token,
        }

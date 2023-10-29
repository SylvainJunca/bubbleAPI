class MockedTMDBClient:
    def search(self, query):
        class ResponseObject:
            @staticmethod
            def json():
                return {"count": 1, "results": [{"id": "movie_1"}]}

        return ResponseObject.json()

    def get_movie_details(self, movie_id=None):
        class ResponseObject:
            @staticmethod
            def json():
                return {"id": movie_id, "title": "title"}

        return ResponseObject.json()

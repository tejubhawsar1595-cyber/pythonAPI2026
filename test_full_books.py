import requests
import pytest

from basic_request import response

base_url = "https://simple-books-api.glitch.me"

class TestGetBooks:

    def test_get_all_books_return_200(self):
        response = requests.get(f"{base_url}/books")
        assert response.status_code == 200

    def test_book_return_list(self):
        response = requests.get(f"{base_url}/books")
        assert isinstance(response.json(),list)

    def test_filter_by_fiction(self):
        response = requests.get(f"{base_url}/books", params={"type": "fiction"})
        books = response.json()
        for book in books:
            assert book["type"] == "fiction", \
            f"if non-fiction books found: {book["name"]}"

    def test_limit_param(self):
        response = requests.get(f"{base_url}/books",params={"limit": 3})
        assert len(response.json())<=3

    def test_limit_param_min(self):
        response = requests.get(f"{base_url}/books",params={"limit": 1})
        assert len(response.json()) == 1

    def test_limit_param_max(self):
        response = requests.get(f"{base_url}/books",params={"limit": 20})
        assert  len(response.json())<=20


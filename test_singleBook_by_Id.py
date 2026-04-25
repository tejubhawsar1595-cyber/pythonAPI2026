import  requests
import pytest

from basic_request import response
from test_books import params

base_url = "https://simple-books-api.glitch.me"


class TestGetSingleBook:
    bookId = 1
    def test_Status_code_200(self):

        response = requests.get(f"{base_url}/books/{self.bookId}")
        assert response.status_code == 200


    def test_id_filed_present(self):
        response = requests.get(f"{base_url}/books/{self.bookId}")
        data = response.json()
        assert data["id"] == self.bookId

    def test_invalid_BookID_Status_code_404(self):
        response = requests.get(f"{base_url}/books/9999")
        assert response.status_code == 404

    def test_time_validation(self):
        response = requests.get(f"{base_url}/books/{self.bookId}")
        assert response.elapsed.total_seconds()<3


    @pytest.mark.parametrize("book_list",[1,2,3,4,5])
    def test_multiple_book_ids(self,book_list):
        response = requests.get(f"{base_url}/books/{book_list}")
        assert response.status_code in [200,404]


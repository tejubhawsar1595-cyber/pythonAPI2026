import requests
import pytest

base_url = "https://simple-books-api.glitch.me"

def test_get_all_books():
    response = requests.get(f"{base_url}/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books,list)   # "Response should be a list
    assert len(books)>0  # "Books list should not be empty"

    # Structure validation
    first_book = books[0]
    assert "id" in first_book
    assert "name" in first_book
    assert "type" in first_book
    assert "available" in first_book


#the end point support 2 optional query support
# 1. 'type' - fiction and non-fiction
#2. 'limit' - number of result(1-20)


params = {
    "type" : "fiction",
    "limit": 5
}

def test_params():
    response = requests.get(f"{base_url}/books",params = params)
    print(response.url)
    print(response.text)
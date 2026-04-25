import requests
import pytest


base_url = "https://simple-books-api.glitch.me"

class Test_API_Status:

    def test_status_code(self):
        response = requests.get(f"{base_url}/status")
        assert response.status_code == 200, \
            f"Expected 200 , got {response.status_code}"


    def test_status_value_ok(self):
        response = requests.get(f"{base_url}/status")
        data = response.json()
        assert data["status"] == "OK"


    def test_response_time_under_3sec(self):
        response = requests.get(f"{base_url}/status")
        assert response.elapsed.total_seconds()<3, \
            f"Api response is slow"

    def test_content_type_json(self):
        response = requests.get(f"{base_url}/status")
        assert "application/json" in response.headers["Content-Type"]






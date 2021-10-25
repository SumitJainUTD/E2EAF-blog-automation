import pytest
import requests


def test_get_health():
    response = requests.get("http://127.0.0.1:3000/api/health/")
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

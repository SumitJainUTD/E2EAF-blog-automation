import pytest
import requests

def test_get_employee():
    response = requests.get("http://127.0.0.1:3000/api/health/")
    print(response.status_code)
    print(response.text)
    assert response.ok
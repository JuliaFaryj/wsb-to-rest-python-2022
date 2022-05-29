# https://docs.github.com/en/rest/repos/repos#list-repositories-for-the-authenticated-user
# tests for authenticated user to list all repos for that user
import requests
from settings.credentials import GITHUB_API_USER
from settings.credentials import GITHUB_API_TOKEN


def test_status_401_for_not_authenticated_user():
    url = "https://api.github.com/user/repos"
    response = requests.get(url)
    assert response.status_code == 401
    jsonBody = response.json()
    assert jsonBody["message"] == "Requires authentication"

def test_status_200_for_authenticated_user():
    url = "https://api.github.com/user/repos"
    # send GET request with credentials
    response = requests.get(url, auth= (GITHUB_API_USER, GITHUB_API_TOKEN))
    # This is valid credentials so expecting status code 200
    assert response.status_code == 200
   # jsonBody = response.json()



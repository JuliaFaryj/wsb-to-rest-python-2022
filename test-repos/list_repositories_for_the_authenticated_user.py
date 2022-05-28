# https://docs.github.com/en/rest/repos/repos#list-repositories-for-the-authenticated-user
# tests for authenticated user to list all repos for that user
import requests


def test_status_401_for_not_authenticated_user():
    url = "https://api.github.com/user/repos"
    response = requests.get(url)
    assert response.status_code == 401
    jsonBody = response.json()
    assert jsonBody["message"] == "Requires authentication"



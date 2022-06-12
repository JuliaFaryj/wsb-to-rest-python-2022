# https://docs.github.com/en/rest/repos/repos#update-a-repository
# test for authenticated user to update a repository

import requests
from settings.credentials import GITHUB_API_USER
from settings.credentials import GITHUB_API_TOKEN

# tests for authenticated user to update already existing private repository
def test_status_200_for_updating_private_repo():
    url = "https://api.github.com/repos/JuliaFaryj/my-python-created-test-private-repo-01"
    dataToSend = {
        "description": "Updating already existing repo to test PATCH REST method"
    }
    response = requests.patch(
        url=url,
        auth=(GITHUB_API_USER, GITHUB_API_TOKEN),
        json=dataToSend)
    response_body = response.json()

    assert response.status_code == 200

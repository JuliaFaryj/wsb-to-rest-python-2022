# https://docs.github.com/en/rest/repos/repos#create-a-repository-for-the-authenticated-user
# tests for authenticated user to create a new repository

import requests
from settings.credentials import GITHUB_API_USER
from settings.credentials import GITHUB_API_TOKEN

def test_status_201_for_new_repo():
    restUrl = "https://api.github.com/user/repos"
    dataToSend = {
        "name": "my-python-created-test-public-repo-01"
    }
    response = requests.post(url=restUrl,
            auth= (GITHUB_API_USER, GITHUB_API_TOKEN),
            json=dataToSend
    )
    assert response.status_code == 201

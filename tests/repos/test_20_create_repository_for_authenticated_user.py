# https://docs.github.com/en/rest/repos/repos#create-a-repository-for-the-authenticated-user
# tests for authenticated user to create a new repository


import requests
from settings.credentials import GITHUB_API_USER
from settings.credentials import GITHUB_API_TOKEN

# tests for authenticated user to create a new public repository
def test_status_201_for_new_public_repo():
    url = "https://api.github.com/user/repos"
    dataToSend = {
        "name": "my-python-created-test-public-repo-01"
    }
    response = requests.post(
            url=url,
            auth=(GITHUB_API_USER, GITHUB_API_TOKEN),
            json=dataToSend)
    response_body = response.json()

    assert response.status_code == 201

# tests for authenticated user to create a new private repository
def test_status_201_for_new_private_repo():
    restUrl = "https://api.github.com/user/repos"
    dataToSend = {
        "name": "my-python-created-test-private-repo-01",
        "private": True
    }
    response = requests.post(
            url=restUrl,
            auth= (GITHUB_API_USER, GITHUB_API_TOKEN),
            json=dataToSend)

    assert response.status_code == 201

# tests for authenticated user to create repository with name already existing
def test_status_422_when_creating_repo_with_name_already_existing():
    restUrl = "https://api.github.com/user/repos"
    dataToSend = {
        "name": "wsb-to-rest-python-2022"
    }
    response = requests.post(
            url=restUrl,
            auth= (GITHUB_API_USER, GITHUB_API_TOKEN),
            json=dataToSend)

    assert response.status_code == 422


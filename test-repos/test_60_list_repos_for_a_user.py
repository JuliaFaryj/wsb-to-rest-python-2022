# https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user
# tests for unauthenticated user to list public repos of other user
import requests
from settings.credentials import GITHUB_API_USER

def test_status_404_for_not_existing_user():
    url = "https://api.github.com/users/USERNAME_not_exists/repos"
    response = requests.get(url)
    assert response.status_code == 404

def test_status_200_for_existing_user():
    url = "https://api.github.com/users/"+GITHUB_API_USER+"/repos"
    response = requests.get(url)
    assert response.status_code == 200

def test_public_repo_exist():
    url = "https://api.github.com/users/"+GITHUB_API_USER+"/repos"
    response = requests.get(url)
    assert response.status_code == 200
    jsonBody = response.json()
    repoExists = False
    for index in range(len(jsonBody)):
        if jsonBody[index]["name"] == "my-python-created-test-public-repo-01":
            repoExists = True
    assert repoExists == True


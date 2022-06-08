# https://docs.github.com/en/rest/repos/repos#get-a-repository
# test for authenticated user to get a repository

import requests
from settings.credentials import GITHUB_API_USER
from settings.credentials import GITHUB_API_TOKEN

def test_status_200_for_existing_private_repo():
    url = "https://api.github.com/repos/JuliaFaryj/my-python-created-test-private-repo-01"
    # send GET request with credentials
    response = requests.get(url, auth= (GITHUB_API_USER, GITHUB_API_TOKEN))
    assert response.status_code == 200
    jsonRepoInfo = response.json()
    assert jsonRepoInfo["name"] == "my-python-created-test-private-repo-01"
    assert jsonRepoInfo["private"] == True




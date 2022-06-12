# https://docs.github.com/en/rest/repos/repos#delete-a-repository
# test for authenticated user to delete a repository

import requests
from settings.credentials import GITHUB_API_USER
from settings.credentials import GITHUB_API_TOKEN

# tests for authenticated user to delete (with status code 204_no content) already existing private repository
def test_status_204_for_deleting_private_repo():
    url = "https://api.github.com/repos/JuliaFaryj/my-python-created-test-private-repo-01"
    response = requests.delete(
        url=url,
        auth=(GITHUB_API_USER, GITHUB_API_TOKEN))

    assert response.status_code == 204
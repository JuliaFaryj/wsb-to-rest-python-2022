import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_delete_pull_request_reviews():
    """"deleting required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_BRANCHES + "/test-branch/protection/required_pull_request_reviews",
                               headers=headers)
    assert response.status_code == 204
    assert response.text == ''
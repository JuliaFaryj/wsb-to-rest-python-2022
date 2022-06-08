import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_get_pull_request_reviews():
    """"getting required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_PROTECTION + "/required_pull_request_reviews",
                            headers=headers)
    assert response.status_code == 200
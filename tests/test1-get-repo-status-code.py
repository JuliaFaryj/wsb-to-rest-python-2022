import requests
from settings.githubconfig import GITHUB_REST_REPO_URL
from settings.credentials import GITHUB_TOKEN


def test_get_repo_status_code():
    """requesting for repository status code when unauthorised"""
    response = requests.get(GITHUB_REST_REPO_URL)
    assert response.status_code == 200


def test_get_repo_status_code_with_auth():
    """requesting for repository status code when authorised"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_REPO_URL, headers=headers)
    assert response.status_code == 200


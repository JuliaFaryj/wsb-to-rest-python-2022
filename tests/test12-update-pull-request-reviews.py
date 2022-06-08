import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_update_pull_request_reviews():
    """"updating required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "dismiss_stale_reviews": True,
        "require_code_owner_reviews": True
    }
    response = requests.patch(GITHUB_REST_URL_BRANCHES + "/test-branch/protection/required_pull_request_reviews",
                              headers=headers, json=data)
    assert response.status_code == 200
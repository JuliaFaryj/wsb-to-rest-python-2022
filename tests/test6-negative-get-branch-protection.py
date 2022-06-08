import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_get_branch_protection(create_branch):
    """get a branch protection rule when it's not created"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_PROTECTION,
                            headers=headers)
    assert response.status_code == 404
    response_body = response.json()
    assert response_body["message"] == "Branch not protected"










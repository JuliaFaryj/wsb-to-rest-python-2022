import requests
import pytest
from branches.settings.credentials_branches import GITHUB_TOKEN
from branches.settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_negative_get_branch_protection(create_branch):
    """get a branch protection rule when it's not created"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_PROTECTION,
                            headers=headers)
    assert response.status_code == 404
    response_body = response.json()
    assert response_body["message"] == "Branch not protected"










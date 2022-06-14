import requests
import pytest
from branches.settings.credentials_branches import GITHUB_TOKEN
from branches.settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_get_branch_protection(update_protection_delete_all):
    """get a branch protection rule information"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_PROTECTION,
                            headers=headers)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["required_signatures"]["enabled"] == False
    assert response_body["enforce_admins"]["enabled"] == True
    assert response_body["required_linear_history"]["enabled"] == False

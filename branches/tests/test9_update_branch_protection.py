import requests
import pytest
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_update_branch_protection(create_branch_delete_all):
    """update  information in a new branch protection rule in the repository"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "required_status_checks": None,
        "enforce_admins": True,
        "required_pull_request_reviews": None,
        "restrictions": None,
        "required_linear_history": None
    }
    response = requests.put(GITHUB_REST_URL_PROTECTION,
                            headers=headers, json=data)
    assert response.status_code == 200

    """"check if branch protection rule is changed"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_PROTECTION,
                            headers=headers)
    response_body = response.json()
    assert response_body["enforce_admins"]["enabled"] == True


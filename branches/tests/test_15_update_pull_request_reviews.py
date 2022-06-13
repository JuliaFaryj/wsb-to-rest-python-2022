import requests
import pytest
from branches.settings.credentials_branches import GITHUB_TOKEN
from branches.settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_update_pull_request_reviews(update_protection_delete_all):
    """"update required_pull_request_reviews rule in the protection rule of a branch"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "dismiss_stale_reviews": True,
        "require_code_owner_reviews": True
    }
    response = requests.patch(GITHUB_REST_URL_PROTECTION + "/required_pull_request_reviews",
                              headers=headers, json=data)
    assert response.status_code == 200

    """"check if branch protection rule is changed"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_PROTECTION + "/required_pull_request_reviews",
                            headers=headers)
    response_body = response.json()
    assert response_body["dismiss_stale_reviews"] == True
    assert response_body["require_code_owner_reviews"] == True

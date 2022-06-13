import requests
import pytest
from branches.settings.credentials_branches import GITHUB_TOKEN
from branches.settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_get_pull_request_reviews(update_protection_delete_all):
    """"get required_pull_request_reviews rule in the protection rule of a branch"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_PROTECTION + "/required_pull_request_reviews",
                            headers=headers)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["dismiss_stale_reviews"] == False
    assert response_body["require_code_owner_reviews"] == False
    assert response_body["required_approving_review_count"] == 1

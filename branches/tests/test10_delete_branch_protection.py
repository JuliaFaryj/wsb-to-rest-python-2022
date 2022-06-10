import requests
import pytest
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_delete_branch_protection(update_protection):
    """"delete branch protection rule"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_PROTECTION,
                               headers=headers)
    assert response.status_code == 204
    assert response.text == ''
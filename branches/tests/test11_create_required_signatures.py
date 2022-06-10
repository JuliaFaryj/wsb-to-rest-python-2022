import requests
import pytest
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_create_required_signatures(signatures_protection_delete_all):
    """"add required_signatures rule in the protection rule of a branch"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.post(GITHUB_REST_URL_PROTECTION + "/required_signatures",
                             headers=headers)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["enabled"] == True



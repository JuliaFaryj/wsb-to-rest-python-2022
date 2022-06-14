import requests
import pytest
from tests.branches.settings.credentials_branches import GITHUB_TOKEN
from tests.branches.settings.githubconfig import GITHUB_REST_URL_PROTECTION


def test_delete_required_signatures(signatures_protection_create):
    """"delete required_signatures rule in the protection rule of a branch"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_PROTECTION + "/required_signatures",
                               headers=headers)
    assert response.status_code == 204
    assert response.text == ''
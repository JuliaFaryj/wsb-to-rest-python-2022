import requests
import pytest
from settings.githubconfig import GITHUB_REST_URL_REF


def test_negative_create_new_branch_no_token(branch_sha):
    """create a new branch in the repository without putting in token"""
    sha = branch_sha
    headers = {
        "Authorization": "token "
    }
    data = {
        "ref": "refs/heads/test-branch",
        "sha": sha
    }
    response = requests.post(GITHUB_REST_URL_REF,
                             headers=headers,
                             json=data)
    assert response.status_code == 401
    response_body = response.json()
    assert response_body["message"] == "Bad credentials"

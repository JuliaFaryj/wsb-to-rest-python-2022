import requests
import pytest
from branches.settings.githubconfig import GITHUB_REST_URL_REF


def test_negative_create_new_branch_no_auth(branch_sha):
    """create a new branch in the repository without authorization"""
    sha = branch_sha
    data = {
        "ref": "refs/heads/test-branch",
        "sha": sha
    }
    response = requests.post(GITHUB_REST_URL_REF,
                             json=data)
    assert response.status_code == 404
    response_body = response.json()
    assert response_body["message"] == "Not Found"

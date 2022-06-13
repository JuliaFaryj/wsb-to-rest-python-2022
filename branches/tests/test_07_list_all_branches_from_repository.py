import requests
import pytest
from branches.settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_list_all_branches_from_repository(create_branches):
    """list all the branches in the repository"""
    response = requests.get(GITHUB_REST_URL_BRANCHES)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]["name"] == "main"
    assert response_body[1]["name"] == "test-branch"
    assert response_body[2]["name"] == "test-branch1"

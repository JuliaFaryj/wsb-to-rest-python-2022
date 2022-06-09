import requests
import pytest
from settings.githubconfig import GITHUB_REST_URL_BRANCH1


def test_get_a_branch_info(create_branch):
    """"get information about a branch in the repository"""
    response = requests.get(GITHUB_REST_URL_BRANCH1)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["name"] == "test-branch"
    assert response_body["commit"]["commit"]["author"]["name"] == "Tatiana Zhukauskene"

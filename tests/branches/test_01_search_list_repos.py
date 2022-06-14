import requests
import pytest
from branches.settings.githubconfig import GITHUB_REST_SEARCH


def test_search_for_a_concrete_repo():
    """"search for a repository for testing"""
    response = requests.get(GITHUB_REST_SEARCH)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["total_count"] == 14
    assert response_body["items"][5]["name"] == "Test-version"













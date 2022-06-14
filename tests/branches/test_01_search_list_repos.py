import requests
import pytest
from tests.branches.settings.githubconfig import GITHUB_REST_SEARCH


def test_search_for_a_concrete_repo():
    """"search for a repository for testing"""
    response = requests.get(GITHUB_REST_SEARCH)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["total_count"] > 0
    items = response_body["items"]
    iterator = (x for x in items if x["name"] == "Test-version")
    item = next(iterator, None)
    assert item is not None













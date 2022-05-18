import requests
from settings.githubconfig import GITHUB_REST_REPO_URL


def test_get_response_status_code():
    response = requests.get(GITHUB_REST_REPO_URL)
    assert response.status_code == 200


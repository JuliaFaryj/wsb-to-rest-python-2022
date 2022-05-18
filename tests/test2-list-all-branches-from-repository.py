import json
import requests
from settings import credentials
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_get_branch_sha():
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    assert response.status_code == 200
    sha = response.json()
    return sha


def test_create_new_branch():
    response = requests.post(GITHUB_REST_URL_REF, auth=(credentials.GITHUB_USER, credentials.GITHUB_PASSWORD),
                             headers={'username': 'token'})
    data = json.dumps({
        "ref": "refs/heads/branch1",
        "sha": "cdcefaccc4e8858f291c40705fab4488fb44ae27"
    })
    assert response.status_code == 201
    response_body = response.json()


def test_list_all_branches_from_repository():
    response = requests.get(GITHUB_REST_URL_BRANCHES)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]["name"] == "main"
    assert response_body[1]["name"] == "branch1"

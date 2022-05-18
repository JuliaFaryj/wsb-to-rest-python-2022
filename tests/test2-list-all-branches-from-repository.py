import requests
from settings import credentials
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_create_branch1_in_repository():
    response = requests.get(GITHUB_REST_URL_REF + "/heads")
    assert response.status_code == 200
    response = requests.post(GITHUB_REST_URL_REF, auth=(credentials.GITHUB_USER, credentials.GITHUB_PASSWORD),
                             headers={'content-type': 'application/json'})
    assert response.status_code == 201
    response_body = response.json()
    var = {
        "ref": "refs/heads/branch1",
        "sha": "<cdcefaccc4e8858f291c40705fab4488fb44ae27>"
    }


def test_list_all_branches_from_repository():
    response = requests.get(GITHUB_REST_URL_BRANCHES)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]["name"] == "branch1"
    assert response_body[1]["name"] == "branch2"
    assert response_body[2]["name"] == "main"

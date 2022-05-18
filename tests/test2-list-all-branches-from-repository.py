import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_get_branch_sha():
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    assert response.status_code == 200
    sha = response.json()
    return sha


def test_create_new_branch1():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "ref": "refs/heads/branch1",
        "sha": "cdcefaccc4e8858f291c40705fab4488fb44ae27"
    }
    response = requests.post(GITHUB_REST_URL_REF,
                             headers=headers,
                             json=data)

    assert response.status_code == 201


def test_create_new_branch2():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "ref": "refs/heads/branch2",
        "sha": "cdcefaccc4e8858f291c40705fab4488fb44ae27"
    }
    response = requests.post(GITHUB_REST_URL_REF,
                             headers=headers,
                             json=data)

    assert response.status_code == 201


def test_list_all_branches_from_repository():
    response = requests.get(GITHUB_REST_URL_BRANCHES)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]["name"] == "branch1"
    assert response_body[1]["name"] == "branch2"
    assert response_body[2]["name"] == "main"


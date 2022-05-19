import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.githubconfig import GITHUB_REST_URL_BRANCH1


def get_branch_sha():
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    data = response.json()
    sha = data["object"]["sha"]
    return sha


def create_new_branch():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    sha = test_preparation_get_branch_sha()
    data = {
        "ref": "refs/heads/new-branch",
        "sha": sha
    }
    requests.post(GITHUB_REST_URL_REF,
                  headers=headers,
                  json=data)


def test_get_a_branch_from_repository():
    response = requests.get(GITHUB_REST_URL_BRANCH1)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["name"] == "new-branch"


def delete_new_branch():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/new-branch", headers=headers)

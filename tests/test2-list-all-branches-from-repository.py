import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_preparation_get_branch_sha():
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    data = response.json()
    sha = data["object"]["sha"]
    return sha


def test_preparation_create_new_branch():
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


def test_preparation_create_new_branch1():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    sha = test_preparation_get_branch_sha()
    data = {
        "ref": "refs/heads/new-branch1",
        "sha": sha
    }
    requests.post(GITHUB_REST_URL_REF,
                  headers=headers,
                  json=data)


def test_list_all_branches_from_repository():
    response = requests.get(GITHUB_REST_URL_BRANCHES)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]["name"] == "main"
    assert response_body[1]["name"] == "new-branch"
    assert response_body[2]["name"] == "new-branch1"


def test_ending_delete_new_branch():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/new-branch", headers=headers)


def test_ending_delete_new_branch1():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/new-branch1", headers=headers)

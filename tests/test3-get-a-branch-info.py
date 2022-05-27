import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.githubconfig import GITHUB_REST_URL_BRANCH1


def get_branch_sha():
    """getting sha of the main branch to create a new branch in the repository"""
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    data = response.json()
    sha = data["object"]["sha"]
    return sha


def create_new_branch():
    """creating a new branch in the repository"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    sha = get_branch_sha()
    data = {
        "ref": "refs/heads/new-branch",
        "sha": sha
    }
    requests.post(GITHUB_REST_URL_REF,
                  headers=headers,
                  json=data)


def test_get_a_branch_from_repository():
    """"getting information about a new-branch in the repository"""
    create_new_branch()
    response = requests.get(GITHUB_REST_URL_BRANCH1)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["name"] == "new-branch"


def delete_new_branch():
    """"deleting new-branch to finish the test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/new-branch", headers=headers)

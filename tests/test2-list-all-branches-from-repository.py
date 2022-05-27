import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


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


def create_new_branch1():
    """creating one more branch in the repository to show the list of them in the next test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    sha = get_branch_sha()
    data = {
        "ref": "refs/heads/new-branch1",
        "sha": sha
    }
    requests.post(GITHUB_REST_URL_REF,
                  headers=headers,
                  json=data)


def test_list_all_branches_from_repository():
    """listing all the branches in the repository"""
    create_new_branch1()
    create_new_branch()
    response = requests.get(GITHUB_REST_URL_BRANCHES)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]["name"] == "main"
    assert response_body[1]["name"] == "new-branch"
    assert response_body[2]["name"] == "new-branch1"


def delete_new_branch():
    """"deleting new-branch to finish the test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/new-branch", headers=headers)


def delete_new_branch1():
    """"deleting new-branch1 to finish the test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/new-branch1", headers=headers)

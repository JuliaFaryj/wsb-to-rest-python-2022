import requests
from settings.githubconfig import GITHUB_REST_URL_REF


def get_branch_sha():
    """getting sha of the main branch to create a new branch in the repository"""
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    data = response.json()
    sha = data["object"]["sha"]
    return sha


def test_negative_create_new_branch_no_auth():
    """creating a new branch in the repository without authorization"""
    sha = get_branch_sha()
    data = {
        "ref": "refs/heads/test-branch",
        "sha": sha
    }
    response = requests.post(GITHUB_REST_URL_REF,
                             json=data)
    assert response.status_code == 404


def test_negative_create_new_branch_no_token():
    """creating a new branch in the repository without putting in token"""
    sha = get_branch_sha()
    headers = {
        "Authorization": "token "
    }
    data = {
        "ref": "refs/heads/test-branch",
        "sha": sha
    }
    response = requests.post(GITHUB_REST_URL_REF,
                             headers=headers,
                             json=data)
    assert response.status_code == 401


def test_negative_create_new_branch_incorrect_token():
    """creating a new branch in the repository with incorrect token"""
    sha = get_branch_sha()
    headers = {
        "Authorization": "token ghp_pusNUAtBf15UYYrDad2zbSuDycjsts09vie8"
    }
    data = {
        "ref": "refs/heads/test-branch",
        "sha": sha
    }
    response = requests.post(GITHUB_REST_URL_REF,
                             headers=headers,
                             json=data)
    assert response.status_code == 401

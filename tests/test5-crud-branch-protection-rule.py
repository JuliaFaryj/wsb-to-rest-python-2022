import json
import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_BRANCHES
from settings.githubconfig import GITHUB_REST_URL_REF


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
        "ref": "refs/heads/branch1",
        "sha": sha
    }
    requests.post(GITHUB_REST_URL_REF,
                  headers=headers,
                  json=data)


def test_get_branch_protection():
    """getting a new branch protection rule in the repository"""
    create_new_branch()
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_BRANCHES + "/branch1/protection",
                            headers=headers)
    assert response.status_code == 200


def test_update_branch_protection():
    """updating  information in a new branch protection rule in the repository"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    payload = {
        "required_signatures": False,
        "enforce_admins": False,
        "required_linear_history": True,
        "allow_force_pushes": False,
        "allow_deletions": False,
        "block_creations": False,
        "required_conversation_resolution": False
    }
    response = requests.put(GITHUB_REST_URL_BRANCHES + "/branch1/protection",
                            headers=headers, params=payload)
    assert response.status_code == 200


def test_delete_branch_protection():
    """"deleting branch protection rule to finish the test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_BRANCHES + "/branch1/protection",
                               headers=headers)
    assert response.status_code == 204


def delete_new_branch():
    """"deleting branch1 to finish the test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/branch1", headers=headers)

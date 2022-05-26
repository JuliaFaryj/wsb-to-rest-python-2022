import json
import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_BRANCHES
from settings.githubconfig import GITHUB_REST_URL_REF


def get_branch_sha():
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    data = response.json()
    sha = data["object"]["sha"]
    return sha


def create_new_branch():
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
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_BRANCHES + "/branch1/protection",
                            headers=headers)
    assert response.status_code == 200


def test_update_branch_protection(false=None, true=None):
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = json.dumps({
        "required_signatures": false,
        "enforce_admins": false,
        "required_linear_history": true,
        "allow_force_pushes": false,
        "allow_deletions": false,
        "block_creations": false,
        "required_conversation_resolution": false
    })
    response = requests.put(GITHUB_REST_URL_BRANCHES + "/branch1/protection",
                            headers=headers, json=data)
    assert response.status_code == 200


def test_delete_branch_protection():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_BRANCHES + "/branch1/protection",
                               headers=headers)
    assert response.status_code == 204


def delete_new_branch():
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/branch1", headers=headers)

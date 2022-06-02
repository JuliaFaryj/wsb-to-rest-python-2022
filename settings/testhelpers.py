import pytest
import requests
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.credentials import GITHUB_TOKEN


def get_branch_sha():
    """getting sha of the main branch to create a new branch in the repository"""
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    data = response.json()
    sha = data["object"]["sha"]
    return sha


def create_new_branch(branch_name):
    """creating a new branch in the repository"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    sha = get_branch_sha()
    data = {
        "ref": "refs/heads/" + branch_name,
        "sha": sha
    }
    requests.post(GITHUB_REST_URL_REF,
                  headers=headers,
                  json=data)


def delete_new_branch(branch_name):
    """"deleting new-branch to finish the test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/" + branch_name, headers=headers)



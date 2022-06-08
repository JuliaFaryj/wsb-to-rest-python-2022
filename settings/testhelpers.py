import pytest
import requests
from settings.githubconfig import GITHUB_REST_URL_REF
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


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


def update_branch_protection(branch_name):
    """updating  information in a new branch protection rule in the repository"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "required_status_checks": None,
        "enforce_admins": True,
        "required_pull_request_reviews": None,
        "restrictions": None
    }
    requests.put(GITHUB_REST_URL_BRANCHES + "/" + branch_name + "/protection",
                 headers=headers, json=data)


def delete_branch_protection(branch_name):
    """"deleting branch protection rule"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_BRANCHES + "/" + branch_name + "/protection",
                    headers=headers)


def create_required_signatures(branch_name):
    """"adding required_signatures rule in the protection rule of a test-branch"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.post(GITHUB_REST_URL_BRANCHES + "/" + branch_name + "/protection/required_signatures",
                  headers=headers)


def delete_required_signatures(branch_name):
    """"deleting required_signatures rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_BRANCHES + "/" + branch_name + "/protection/required_signatures",
                    headers=headers)

import requests
from tests.branches.settings.githubconfig import GITHUB_REST_URL_REF
from tests.branches.settings.credentials_branches import GITHUB_TOKEN
from tests.branches.settings.githubconfig import GITHUB_REST_URL_BRANCHES


def get_branch_sha():
    """get sha of the main branch to create a new branch in the repository"""
    response = requests.get(GITHUB_REST_URL_REF + "/heads/main")
    response_body = response.json()
    sha = response_body["object"]["sha"]
    return sha


def create_new_branch(branch_name):
    """create a new branch in the repository"""
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
    """"delete a new branch to finish the test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_REF + "/heads/" + branch_name, headers=headers)


def update_branch_protection(branch_name):
    """add and update  information in a new branch protection rule in the repository"""
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
    """"delete branch protection rule"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_BRANCHES + "/" + branch_name + "/protection",
                    headers=headers)


def create_required_signatures(branch_name):
    """"add required_signatures rule in the protection rule"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.post(GITHUB_REST_URL_BRANCHES + "/" + branch_name + "/protection/required_signatures",
                  headers=headers)


def delete_required_signatures(branch_name):
    """"delete required_signatures in the protection rule"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    requests.delete(GITHUB_REST_URL_BRANCHES + "/" + branch_name + "/protection/required_signatures",
                    headers=headers)


def create_pull_request_reviews(branch_name):
    """"create and update required_pull_request_reviews in the protection rule"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "dismiss_stale_reviews": True,
        "require_code_owner_reviews": True
    }
    requests.patch(GITHUB_REST_URL_BRANCHES + "/" + branch_name + "/required_pull_request_reviews",
                   headers=headers, json=data)

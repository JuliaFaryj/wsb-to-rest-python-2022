import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_update_branch_protection(create_branch_no_delete):
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
    response = requests.put(GITHUB_REST_URL_BRANCHES + "/test-branch/protection",
                            headers=headers, json=data)
    assert response.status_code == 200


def test_get_branch_protection():
    """getting a new branch protection rule in the repository"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_BRANCHES + "/test-branch/protection",
                            headers=headers)
    assert response.status_code == 200


def test_create_required_signatures():
    """"adding required_signatures rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.post(GITHUB_REST_URL_BRANCHES + "/test-branch/protection/required_signatures",
                             headers=headers)
    assert response.status_code == 200


def test_delete_required_signatures():
    """"deleting required_signatures rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_BRANCHES + "/test-branch/protection/required_signatures",
                               headers=headers)
    assert response.status_code == 204


def test_get_pull_request_reviews():
    """"getting required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_BRANCHES + "/test-branch/protection/required_pull_request_reviews",
                            headers=headers)
    assert response.status_code == 200


def test_update_pull_request_reviews():
    """"updating required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    data = {
        "dismiss_stale_reviews": True,
        "require_code_owner_reviews": True
    }
    response = requests.patch(GITHUB_REST_URL_BRANCHES + "/test-branch/protection/required_pull_request_reviews",
                              headers=headers, json=data)
    assert response.status_code == 200


def test_delete_pull_request_reviews():
    """"deleting required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_BRANCHES + "/test-branch/protection/required_pull_request_reviews",
                               headers=headers)
    assert response.status_code == 204


def test_delete_branch_protection(delete_branch):
    """"deleting branch protection rule to finish the test"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_BRANCHES + "/test-branch/protection",
                               headers=headers)
    assert response.status_code == 204

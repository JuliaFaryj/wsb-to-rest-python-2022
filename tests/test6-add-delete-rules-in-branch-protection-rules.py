import requests
from settings.credentials import GITHUB_TOKEN
from settings.githubconfig import GITHUB_REST_URL_BRANCHES


def test_create_required_signatures():
    """"adding required_signatures rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.post(GITHUB_REST_URL_BRANCHES + "/branch1/protection/required_signatures",
                             headers=headers)
    assert response.status_code == 200


def test_delete_required_signatures():
    """"deleting required_signatures rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_BRANCHES + "/branch1/protection/required_signatures",
                               headers=headers)
    assert response.status_code == 204


def test_get_pull_request_reviews():
    """"getting required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.get(GITHUB_REST_URL_BRANCHES + "/branch1/protection/required_pull_request_reviews",
                            headers=headers)
    assert response.status_code == 200


def test_update_pull_request_reviews():
    """"updating required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.patch(GITHUB_REST_URL_BRANCHES + "/branch1/protection/required_pull_request_reviews",
                              headers=headers)
    assert response.status_code == 200


def test_delete_pull_request_reviews():
    """"deleting required_pull_request_reviews rule in the protection rule of a branch1"""
    headers = {
        "Authorization": "token " + GITHUB_TOKEN
    }
    response = requests.delete(GITHUB_REST_URL_BRANCHES + "/branch1/protection/required_pull_request_reviews",
                               headers=headers)
    assert response.status_code == 204

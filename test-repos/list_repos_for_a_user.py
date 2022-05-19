# https://docs.github.com/en/rest/repos/repos#list-repositories-for-a-user
import requests

def test_status_404_for_not_existing_user():
    url = "https://api.github.com/users/USERNAME_not_exists/repos"
    response = requests.get(url)
    assert response.status_code == 404

def test_status_200_for_existing_user():
    url = "https://api.github.com/users/JuliaFaryj/repos"
    response = requests.get(url)
    assert response.status_code == 200

def test_Publiczne_repo_exist():
    url = "https://api.github.com/users/JuliaFaryj/repos"
    response = requests.get(url)
    assert response.status_code == 200
    jsonBody = response.json()
    assert jsonBody[0]["name"] == "Publiczne"

def test_test_pubic_repo_exist():
    url = "https://api.github.com/users/JuliaFaryj/repos"
    response = requests.get(url)
    assert response.status_code == 200
    jsonBody = response.json()
    assert jsonBody[1]["name"] == "test-pubic"

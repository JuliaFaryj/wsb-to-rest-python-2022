import requests

from tests.Commits.settings import TOKEN

#Test using GET
def test_get_author_of_commit():
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + TOKEN}
    url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/commits/fcdf6e3112e594e250481d20eb5c9203d818dbc0"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["commit"]["message"] == "Dodanie dwóch plików do brancha FunkcjaGet"
    assert response_body["commit"]["author"]["name"] == 'Aleksandra Wszeborowska'


import requests
from tests.Commits.settings import TOKEN


# Test using POST
def test_create_commit_comment():
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + TOKEN}
    data = {
        "body": "New comment is done!",
        "path": "GETcommits/lista.txt"
    }
    url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/commits/fcdf6e3112e594e250481d20eb5c9203d818dbc0/comments"
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201


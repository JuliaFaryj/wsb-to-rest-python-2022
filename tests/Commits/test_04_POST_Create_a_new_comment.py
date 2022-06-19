import requests
from settings import TOKEN


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
    delete_commit_comment()


def get_comment_id():
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + TOKEN}
    url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/comments"
    response = requests.get(url, headers=headers)
    response_body = response.json()
    comment_id = response_body[22]["id"]
    return comment_id


def delete_commit_comment():
    comment_id = get_comment_id()
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + TOKEN}
    url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/comments/" + str(comment_id)
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204

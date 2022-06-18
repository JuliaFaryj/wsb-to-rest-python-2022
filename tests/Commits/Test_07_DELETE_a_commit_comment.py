from settings import TOKEN

import requests

#Test using DELETE
def test_delete_commit_comment():
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + TOKEN}
    data = {"body": "To jest aktualizacja nr 1 komentarza1."}
    url = url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/comments/" + comment_id
    response = requests.delete(url, headers=headers, json=data)
    assert response.status_code == 204

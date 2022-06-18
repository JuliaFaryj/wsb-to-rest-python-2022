from settings import TOKEN

import requests

#Test using PATCH
def test_update_commit_comment():
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + TOKEN}
    data = {"body": "To jest aktualizacja nr 1 komentarza1."}

    url = url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/comments/76208177"
    response = requests.patch(url, headers=headers, json=data)
    assert response.status_code == 200


import requests

from tests.Commits.settings import TOKEN

#Test using GET
def test_get_list_of_comments():
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + TOKEN}
    url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/comments"
    response = requests.get(url, headers=headers)
    assert response.json()
    assert response.status_code == 200



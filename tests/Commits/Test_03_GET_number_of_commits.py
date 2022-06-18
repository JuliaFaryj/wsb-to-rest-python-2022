import requests

from settings import TOKEN

#Test using GET number of commits
def test_get_number_of_commits():
    headers = {"Accept": "application/vnd.github.v3+json", "Authorization": "token " + TOKEN}
    url = "https://api.github.com/repos/AleksandraWszeborowska/Windows/commits/fcdf6e3112e594e250481d20eb5c9203d818dbc0"
    response = requests.get(url, headers=headers)

    jsonCommitInfo = response.json()
    assert len(jsonCommitInfo)


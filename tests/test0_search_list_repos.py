import requests


def test_search_for_a_concrete_repo():
    """"search for a repository for testing"""
    url = "https://api.github.com/search/repositories?q=user:TatZhuk&sort=updateds&per_page=5&"
    response = requests.get(url)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["total_count"] == 2
    assert response_body["items"][0]["name"] == "Test-version"













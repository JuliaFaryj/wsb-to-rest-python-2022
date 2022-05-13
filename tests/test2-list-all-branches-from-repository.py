import requests


def test_list_all_branches_from_repository():
    response = requests.get('https://api.github.com/repos/TatZhuk/Test-version/branches')
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]["name"] == "branch1"
    assert response_body[1]["name"] == "branch2"
    assert response_body[2]["name"] == "main"

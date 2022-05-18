import requests


def test_get_a_branch_from_repository():
    response = requests.get('https://api.github.com/repos/TatZhuk/Test-version/branches/branch1')
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["name"] == "branch1"

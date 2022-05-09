import requests

def test_list_all_branches_from_repository ():
    response = requests.get('https://api.github.com/repos/TatZhuk/Test-version/branches')
    response_body = response.json()
    print()


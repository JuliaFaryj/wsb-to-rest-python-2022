import requests

def test_get_response_status_code():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    r.status_code == 200

def test_list_all_branches_():
    r = requests.get ('https://api.github.com/TatZhuk/Test-version/branches, auth=('user', 'pass'))
    r.status_code == 200


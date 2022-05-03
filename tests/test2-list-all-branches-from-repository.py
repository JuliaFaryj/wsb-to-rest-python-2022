import requests

def test_list_all_branches_():
    r = requests.get ('https://api.github.com/TatZhuk/wsb-to-rest-python-2022/branches, auth=('user', 'pass'))
    r.status_code == 200
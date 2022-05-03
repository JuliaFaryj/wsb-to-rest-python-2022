import requests

def test_get_response_status_code():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    r.status_code == 200
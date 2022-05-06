import requests

def test_get_response_status_code():
    r = requests.get('https://api.github.com/TatZhuk/Test-version', auth=('user', 'pass'))
    r.status_code == 200
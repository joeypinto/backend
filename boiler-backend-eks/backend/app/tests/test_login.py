import pprint
import requests as r
from requests.structures import CaseInsensitiveDict

ENDPOINT = 'http://localhost:8000/api/v1'


USERNAME = 'user23@example.com'
PASSWORD = 'password'


# Test Post Open
def test_user_create(client):
    payload_post = {
        "password": PASSWORD,
        "email": USERNAME,
        "username": "string"
    }

    print('Post')
    response_post = r.post(f'{ENDPOINT}/users/open', json=payload_post)
    assert response_post.status_code == 200


# Test Login
def test_user_login():
    payload_post = {
        "grant_type": "",
        "username": USERNAME,
        "password": PASSWORD,
        "scope": "",
        "client_id": "",
        "client_secret": "",
    }

    print('Login')
    response_post = r.post(f'{ENDPOINT}/login/access-token', data=payload_post)
    pprint.pprint(response_post.json())
    assert response_post.status_code == 200
    return response_post.json()['access_token']



# Test Token
def test_user_post(client):
    token = test_user_login()
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    print('Post')
    response_post = r.post(f'{ENDPOINT}/login/test-token', headers=headers)
    pprint.pprint(response_post.json())
    assert response_post.status_code == 200

import pprint
import requests as r
from requests.structures import CaseInsensitiveDict

ENDPOINT = 'http://localhost:8000/api/v1'


USERNAME = 'user24@example.com'
PASSWORD = 'password'


# Test Get
def test_user_get_0(client):
    response_get = r.get(f'{ENDPOINT}/users')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Post Open
def test_user_post_open(client):
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


# Test Get
def test_user_get_1(client):
    response_get = r.get(f'{ENDPOINT}/users')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Post
def test_user_post(client):
    token = test_user_login()
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    payload_post = {
        "email": "userAToddA@example.com",
        "is_active": True,
        "username": "string",
        "password": "string"
    }
    print('Post')
    response_post = r.post(f'{ENDPOINT}/users', json=payload_post, headers=headers)
    pprint.pprint(response_post.json())
    assert response_post.status_code == 200


# Test Get by Id
def test_user_get_id(client):
    token = test_user_login()
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    response_get = r.get(f'{ENDPOINT}/users')
    id = (response_get.json()[0]['id'])

    print('Get by Id')
    response_get = r.get(f'{ENDPOINT}/users/{id}', headers=headers)
    print(response_get.json())


# Test Get Current User
def test_user_get_id(client):
    token = test_user_login()
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    print('Get Current User')
    response_get = r.get(f'{ENDPOINT}/users/me', headers=headers)
    print(response_get.json())


# Test Get
def test_user_get_2(client):
    response_get = r.get(f'{ENDPOINT}/users')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Put
def test_user_put(client):
    token = test_user_login()
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    response_get = r.get(f'{ENDPOINT}/users')
    id = (response_get.json()[0]['id'])
    
    payload_put = {
        "email": "userj@example.com",
        "is_active": True,
        "username": "string",
        "password": "string"
    }
    print('Put')
    response_put = r.put(f'{ENDPOINT}/users/{id}', json=payload_put, headers=headers)
    pprint.pprint(response_put.json())
    assert response_put.status_code == 200


# Test Get
def test_user_get_3(client):
    response_get = r.get(f'{ENDPOINT}/users')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Put
def test_user_put(client):
    token = test_user_login()
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {token}"

    response_get = r.get(f'{ENDPOINT}/users')
    id = (response_get.json()[0]['id'])
    
    payload_put = {
        "password": "string",
        "username": "string",
        "email": "alteringCurrent@example.com"
    }
    print('Put')
    response_put = r.put(f'{ENDPOINT}/users/me', json=payload_put, headers=headers)
    pprint.pprint(response_put.json())
    assert response_put.status_code == 200


# Test Get
def test_user_get_4(client):
    response_get = r.get(f'{ENDPOINT}/users')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Delete
def test_user_delete(client):
    response_get = r.get(f'{ENDPOINT}/users')
    id = (response_get.json()[0]['id'])
    response_delete = r.delete(f'{ENDPOINT}/users/{id}')
    if response_delete.status_code == 405:
        assert response_delete.status_code == 405
        print('Has no Delete Function')
    else:
        assert response_delete.status_code == 200


# Test Get
def test_user_get_5(client):
    response_get = r.get(f'{ENDPOINT}/users')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200

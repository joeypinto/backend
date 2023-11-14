import pprint
import requests as r

ENDPOINT = 'http://localhost:8000/api/v1'

# Test Get
def test_role_get_0(client):
    response_get = r.get(f'{ENDPOINT}/roles')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Post
def test_role_post_0(client):
    payload_post = {
        "name": "Outro",
        "description": "string"
    },
    response_post = r.post(f'{ENDPOINT}/roles', json=payload_post)
    assert response_post.status_code == 200


# Test Get
def test_role_get_1(client):
    response_get = r.get(f'{ENDPOINT}/roles')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Put
def test_role_put(client):
    response_get = r.get(f'{ENDPOINT}/roles')
    id = (response_get.json()[0]['id'])
    payload_put = {
        "name": "Roles",
        "description": "Roles"
    }
    response_put = r.put(f'{ENDPOINT}/roles/{id}', json=payload_put)
    print('Put')
    pprint.pprint(response_put.json())
    assert response_put.status_code == 200


# Test Get
def test_role_get_2(client):
    response_get = r.get(f'{ENDPOINT}/roles')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Delete
def test_role_delete(client):
    response_get = r.get(f'{ENDPOINT}/roles')
    id = (response_get.json()[0]['id'])
    response_delete = r.delete(f'{ENDPOINT}/roles/{id}')
    if response_delete.status_code == 405:
        assert response_delete.status_code == 405
        print('Has no Delete Function')
    else:
        assert response_delete.status_code == 200


# Test Get
def test_role_get_3(client):
    response_get = r.get(f'{ENDPOINT}/roles')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Post    
def test_role_post_1(client):
    payload_post = {
        "name": "Role",
        "description": "string"
    },
    response_post = r.post(f'{ENDPOINT}/roles', json=payload_post)
    assert response_post.status_code == 200
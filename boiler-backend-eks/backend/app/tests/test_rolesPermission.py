import pprint
import requests as r

ENDPOINT = 'http://localhost:8000/api/v1'

# Test Get
def test_role_permission_get_0(client):
    response_get = r.get(f'{ENDPOINT}/roles')
    id = (response_get.json()[0]['id'])

    response_get = r.get(f'{ENDPOINT}/role_permissions/{id}')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200


# Test Put
def test_role_permission_put(client):
    response_get_permission = r.get(f'{ENDPOINT}/permissions')
    id_permission = (response_get_permission.json()[0]['id'])

    response_get_role = r.get(f'{ENDPOINT}/roles')
    role_id = (response_get_role.json()[0]['id'])
    
    payload_put = [
        {
            "name": "aaastring",
            "description": "string",
            "id": id_permission,
        }
    ]
    response_put = r.put(f'{ENDPOINT}/role_permissions/{role_id}', json=payload_put)
    print('Put')
    pprint.pprint(response_put.json())
    assert response_put.status_code == 200


# Test Get
def test_role_permission_get_2(client):
    response_get = r.get(f'{ENDPOINT}/roles')
    id = (response_get.json()[0]['id'])

    response_get = r.get(f'{ENDPOINT}/role_permissions/{id}')
    print('Get')
    pprint.pprint(response_get.json())
    assert response_get.status_code == 200

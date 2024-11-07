import requests


URL = 'http://167.172.172.115:52353'


def create_obj():
    payload = {
        "name": "Someone object",
        "data": {"color": "white", "size": "big"}
    }
    response = requests.post(f'{URL}/object', json=payload)
    assert response.status_code == 200, 'Incorrect response status code'
    return response.json().get('id')


def edit_obj_with_put_method():
    obj_id = create_obj()
    new_payload = {
        "name": "Another object",
        "data": {"color": "green", "size": "small"}
    }
    response = requests.put(f'{URL}/object/{obj_id}', json=new_payload)
    assert response.status_code == 200, 'Incorrect response status code'
    assert response.json().get('name') == new_payload.get('name')
    assert response.json().get('data') == new_payload.get('data')


def edit_obj_with_patch_method():
    obj_id = create_obj()
    new_payload = {
        "name": "One else object",
    }
    response = requests.patch(f'{URL}/object/{obj_id}', json=new_payload)
    assert response.status_code == 200, 'Incorrect response status code'
    assert response.json().get('name') == new_payload.get('name')


def delete_obj():
    obj_id = create_obj()
    response = requests.delete(f'{URL}/object/{obj_id}')
    assert response.status_code == 200, 'Incorrect response status code'


create_obj()
edit_obj_with_put_method()
edit_obj_with_patch_method()
delete_obj()

import requests
import pytest

from data import Objects, Urls


@pytest.mark.critical
@pytest.mark.parametrize('payload', [Objects.obj_1, Objects.obj_2, Objects.obj_3])
def test_create_objs(payload, start_test_session, start_test):
    response = requests.post(f'{Urls.BASE_URL}/object', json=payload)

    assert response.status_code == 200, 'Incorrect response status code'
    assert response.json().get('color') == payload.get('color'), 'Incorrect color'
    assert response.json().get('size') == payload.get('size'), 'Incorrect size'


def test_edit_obj_with_put_method(new_obj_id, start_test_session, start_test):
    new_payload = {
        "name": "Another object",
        "data": {"color": "green", "size": "small"}
    }
    response = requests.put(f'{Urls.BASE_URL}/object/{new_obj_id}', json=new_payload)

    assert response.status_code == 200, 'Incorrect response status code'
    assert response.json().get('name') == new_payload.get('name')
    assert response.json().get('data') == new_payload.get('data')


def test_edit_obj_with_patch_method(new_obj_id, start_test_session, start_test):
    new_payload = {
        "name": "One else object",
    }
    response = requests.patch(f'{Urls.BASE_URL}/object/{new_obj_id}', json=new_payload)

    assert response.status_code == 200, 'Incorrect response status code'
    assert response.json().get('name') == new_payload.get('name')


@pytest.mark.medium
def test_delete_obj(start_test_session, start_test):
    create_response = requests.post(f'{Urls.BASE_URL}/object', json=Objects.obj_3)
    obj_id = create_response.json().get('id')

    response = requests.delete(f'{Urls.BASE_URL}/object/{obj_id}')
    assert response.status_code == 200, 'Incorrect response status code'

import pytest
import requests
import allure

from data import Objects, Urls


@pytest.mark.critical
@pytest.mark.parametrize('payload', [Objects.obj_1, Objects.obj_2, Objects.obj_3])
@allure.title('Check of successful creating an object')
@allure.feature('POSTs')
@allure.story('Create an object')
def test_create_objs(payload, start_test_session, start_test):
    with allure.step('Run request to create an object'):
        response = requests.post(f'{Urls.BASE_URL}/object', json=payload)

    with allure.step('Check that response status code is 200'):
        assert response.status_code == 200, 'Incorrect response status code'
    with allure.step('Check that name of the created object is correct'):
        assert response.json().get('name') == payload.get('name')
    with allure.step('Check that data of the created object is correct'):
        assert response.json().get('data') == payload.get('data')


@allure.title('Check of successful editing the object with PUT')
@allure.feature('PUTs')
@allure.story('Edit the object')
def test_edit_obj_with_put_method(new_obj_id, start_test_session, start_test):
    with (allure.step('Prepare data for edit the object with PUT')):
        new_payload = {
            "name": "Another object",
            "data": {"color": "green", "size": "small"}
        }
    with allure.step('Run request to edit the object with PUT'):
        response = requests.put(f'{Urls.BASE_URL}/object/{new_obj_id}', json=new_payload)

    with allure.step('Check that response status code is 200'):
        assert response.status_code == 200, 'Incorrect response status code'
    with allure.step('Check that name of the created object is correct'):
        assert response.json().get('name') == new_payload.get('name')
    with allure.step('Check that data of the created object is correct'):
        assert response.json().get('data') == new_payload.get('data')


@allure.title('Check of successful editing the object with PATCH')
@allure.feature('PATCHs')
@allure.story('Edit the object')
def test_edit_obj_with_patch_method(new_obj_id, start_test_session, start_test):
    with (allure.step('Prepare data for edit the object with PATCH')):
        new_payload = {
            "name": "One else object",
        }
    with allure.step('Run request to edit the object with PATCH'):
        response = requests.patch(f'{Urls.BASE_URL}/object/{new_obj_id}', json=new_payload)

    with allure.step('Check that response status code is 200'):
        assert response.status_code == 200, 'Incorrect response status code'
    with allure.step('Check that data of the created object is correct'):
        assert response.json().get('name') == new_payload.get('name')


@pytest.mark.medium
@allure.title('Check of successful deleting the object')
@allure.feature('DELETEs')
@allure.story('DELETE the object')
def test_delete_obj(start_test_session, start_test):
    with allure.step('Run request to create an object'):
        create_response = requests.post(f'{Urls.BASE_URL}/object', json=Objects.obj_3)
    with allure.step('Get id of the created object'):
        obj_id = create_response.json().get('id')

    with allure.step('Run request to delete the object'):
        response = requests.delete(f'{Urls.BASE_URL}/object/{obj_id}')
    with allure.step('Check that response status code is 200'):
        assert response.status_code == 200, 'Incorrect response status code'

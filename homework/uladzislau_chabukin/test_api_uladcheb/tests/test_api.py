import pytest
import allure

from test_api_uladcheb.data import Objects


@pytest.mark.critical
@pytest.mark.parametrize('payload', [Objects.obj_1, Objects.obj_2, Objects.obj_3])
@allure.title('Check of successful creating an object')
@allure.feature('POSTs')
@allure.story('Create an object')
def test_create_objs(create_object_endpoint, payload):
    create_object_endpoint.create_object(payload)

    create_object_endpoint.check_object_response(payload)


@allure.title('Check of successful editing the object with PUT')
@allure.feature('PUTs')
@allure.story('Edit the object')
def test_edit_obj_with_put_method(edit_object_with_put_endpoint, new_obj_id):
    new_payload = {
        "name": "Another object",
        "data": {"color": "green", "size": "small"}
    }
    edit_object_with_put_endpoint.edit_object(new_payload, new_obj_id)

    edit_object_with_put_endpoint.check_object_response(new_payload)


@allure.title('Check of successful editing the object with PATCH')
@allure.feature('PATCHs')
@allure.story('Edit the object')
def test_edit_obj_with_patch_method(edit_object_with_patch_endpoint, new_obj_id):
    new_payload = {
        "name": "One else object",
    }
    edit_object_with_patch_endpoint.edit_object(new_payload, new_obj_id)

    edit_object_with_patch_endpoint.check_status_code_is_200()
    edit_object_with_patch_endpoint.check_object_name(new_payload)


@pytest.mark.medium
@allure.title('Check of successful deleting the object')
@allure.feature('DELETEs')
@allure.story('DELETE the object')
def test_delete_obj(create_object_endpoint, delete_object_endpoint):
    create_object_endpoint.create_object(Objects.obj_3)
    obj_id = create_object_endpoint.get_obj_id()

    delete_object_endpoint.delete_object(obj_id)

    delete_object_endpoint.check_status_code_is_200()

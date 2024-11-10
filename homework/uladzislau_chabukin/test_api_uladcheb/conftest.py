import random

import pytest
from faker import Faker

from endpoints.create_object_endpoint import CreateObject
from endpoints.edit_object_with_put_endpoint import EditObjectWithPut
from endpoints.delete_object_endpoint import DeleteObjectEndpoint
from endpoints.edit_object_with_patch_endpoint import EditObjectWithPatch

fake = Faker()


@pytest.fixture
def create_object_endpoint():
    return CreateObject()


@pytest.fixture
def edit_object_with_put_endpoint():
    return EditObjectWithPut()


@pytest.fixture
def edit_object_with_patch_endpoint():
    return EditObjectWithPatch()


@pytest.fixture
def delete_object_endpoint():
    return DeleteObjectEndpoint()


@pytest.fixture()
def new_obj_id(create_object_endpoint, delete_object_endpoint):
    payload = {
        "name": fake.name(),
        "data": {"color": f"{fake.color()}", "size": f"{random.choice(['big', 'small', 'medium'])}"}
    }
    create_object_endpoint.create_object(payload)
    create_object_endpoint.check_status_code_is_200()

    obj_id = create_object_endpoint.get_obj_id()
    yield obj_id

    delete_object_endpoint.delete_object(obj_id)
    delete_object_endpoint.check_status_code_is_200()

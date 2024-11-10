import random

import pytest
import requests
from faker import Faker

from data import Urls

fake = Faker()


@pytest.fixture(scope='session')
def start_test_session():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture(scope='function')
def start_test():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture()
def new_obj_id():
    payload = {
        "name": fake.name(),
        "data": {"color": f"{fake.color()}", "size": f"{random.choice(['big', 'small', 'medium'])}"}
    }
    response = requests.post(f'{Urls.BASE_URL}/object', json=payload)
    assert response.ok, "No created obj"

    obj_id = response.json().get('id')
    yield obj_id

    response = requests.delete(f'{Urls.BASE_URL}/object/{obj_id}')
    assert response.ok, "No deleted obj"

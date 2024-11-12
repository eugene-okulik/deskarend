import random

from locust import HttpUser, task
from faker import Faker

fake = Faker()


class CreateAndDeleteObjectUser(HttpUser):
    @task
    def create_and_delete_object(self):
        payload = {
            "name": fake.name(),
            "data": {"color": f"{fake.color()}", "size": f"{random.choice(['big', 'small', 'medium'])}"}
        }
        response = self.client.post('/object', json=payload)
        obj_id = response.json().get('id')

        self.client.delete(f'/object/{obj_id}')


class EditObjectUser(HttpUser):
    obj_id = None

    def on_start(self) -> None:
        payload = {
            "name": fake.name(),
            "data": {"color": f"{fake.color()}", "size": f"{random.choice(['big', 'small', 'medium'])}"}
        }
        response = self.client.post('/object', json=payload)
        self.obj_id = response.json().get('id')

    @task
    def edit_obj_with_put_method(self):
        new_payload = {
            "name": fake.name(),
            "data": {"color": f"{fake.color()}", "size": f"{random.choice(['big', 'small', 'medium'])}"}
        }
        self.client.put(f'/object/{self.obj_id}', json=new_payload)

    @task
    def edit_obj_name_with_patch_method(self):
        new_payload = {
            "name": fake.name()
        }
        self.client.patch(f'/object/{self.obj_id}', json=new_payload)

    @task
    def edit_obj_data_with_patch_method(self):
        new_payload = {
            "data": {"color": f"{fake.color()}", "size": f"{random.choice(['big', 'small', 'medium'])}"}
        }
        self.client.patch(f'/object/{self.obj_id}', json=new_payload)

    def on_stop(self):
        self.client.delete(f'/object/{self.obj_id}')

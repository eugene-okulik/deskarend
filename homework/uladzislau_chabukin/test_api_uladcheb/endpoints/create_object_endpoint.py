import allure
import requests

from test_api_uladcheb.endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):
    @allure.step('Create a new object')
    def create_object(self, payload):
        self.response = requests.post(f'{self.BASE_URL}/object', json=payload)
        self.response_json = self.response.json()

    def get_obj_id(self):
        return self.response_json.get('id')

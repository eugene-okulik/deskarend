import allure
import requests

from endpoints.base_endpoint import BaseEndpoint


class EditObjectWithPut(BaseEndpoint):

    @allure.step('Edit the object')
    def edit_object(self, payload, obj_id):
        self.response = requests.put(f'{self.BASE_URL}/object/{obj_id}', json=payload)
        self.response_json = self.response.json()

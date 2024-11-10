import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class EditObjectWithPatch(BaseEndpoint):
    @allure.step('Edit the object')
    def edit_object(self, new_payload, obj_id):
        self.response = requests.patch(f'{self.BASE_URL}/object/{obj_id}', json=new_payload)
        self.response_json = self.response.json()

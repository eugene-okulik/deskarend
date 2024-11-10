import requests

from test_api_uladcheb.endpoints.base_endpoint import BaseEndpoint


class DeleteObjectEndpoint(BaseEndpoint):

    def delete_object(self, obj_id):
        self.response = requests.delete(f'{self.BASE_URL}/object/{obj_id}')

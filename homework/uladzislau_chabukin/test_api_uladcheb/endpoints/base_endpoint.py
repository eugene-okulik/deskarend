import allure


class BaseEndpoint:
    BASE_URL = 'http://167.172.172.115:52353'
    response = None
    response_json = None

    @allure.step('Check response status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, 'Response status code is not 200'

    @allure.step('Check that name of the object is correct')
    def check_object_name(self, payload):
        assert self.response_json.get('name') == payload.get('name')

    @allure.step('Check that data of the object is correct')
    def check_object_data(self, payload):
        assert self.response_json.get('data') == payload.get('data')

    @allure.step('Check that response of the object is correct')
    def check_object_response(self, payload):
        self.check_status_code_is_200()
        self.check_object_name(payload)
        self.check_object_data(payload)

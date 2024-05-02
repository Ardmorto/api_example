import requests
from test_data import payloads, headers
from endpoints.json_schemas import AuthData


class Authorize():
    def get_token(self):
        self.response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=payloads.credentials,
            headers=headers.default_header
        )
        if self.response.status_code == 200:
            self.data = AuthData(**self.response.json())
        return self.data.token

    def check_response_is_200(self):
        assert self.response.status_code == 200

    def check_username(self):
        assert self.data.user == payloads.credentials['name']
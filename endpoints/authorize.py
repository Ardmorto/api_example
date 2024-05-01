import requests
from test_data import payloads, headers
from endpoints.base_endpoint import BaseEndpoint
from endpoints.json_schemas import AuthData

class Authorize(BaseEndpoint):
    def get_token(self):
        self.response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=payloads.credentials,
            headers=headers.default_header
        )
        if self.response.status_code == 200:
            self.data = AuthData(**self.response.json())

    def check_username(self, username):
        assert self.data.user == username
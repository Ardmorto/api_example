import requests
from test_data import payloads, headers
from endpoints.base_endpoint import BaseEndpoint
from endpoints.json_schemas import DefaultData

class AddMeme(BaseEndpoint):

    def add_new_meme(self, payload=None):
        payload = payload if payload else payloads.default_payload
        headers.default_header.update(self.token)
        self.response = requests.post(
            'http://167.172.172.115:52355/meme',
            json=payload,
            headers=headers.default_header
        )
        if self.response.status_code == 200:
            self.data = DefaultData(**self.response.json())

    def check_id_assigned(self):
        assert self.data.id != None

    def check_username_is_correct(self):
        assert self.data.updated_by == payloads.credentials['name']
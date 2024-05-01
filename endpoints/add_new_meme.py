import requests
from test_data import payloads, headers
from endpoints.base_endpoint import BaseEndpoint

class AddMeme(BaseEndpoint):

    def add_new_meme(self):
        headers.default_header.update(self.token)
        self.response = requests.post(
            'http://167.172.172.115:52355/meme',
            json=payloads.default_payload,
            headers=headers.default_header
        )
        self.data = self.response.json()
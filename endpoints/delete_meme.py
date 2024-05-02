import requests
from test_data import payloads, headers
from endpoints.base_endpoint import BaseEndpoint

class DeleteMeme(BaseEndpoint):
    def delete_meme(self, id):
        headers.default_header.update(self.token)
        self.response = requests.delete(
            f'http://167.172.172.115:52355/meme/{id}',
            headers=headers.default_header
        )
import requests
from test_data import payloads, headers
from endpoints.base_endpoint import BaseEndpoint

class UpdateMeme(BaseEndpoint):
    def update_meme(self, id_dict):
        headers.default_header.update(self.token)
        payloads.updated_payload.update(id_dict)

        self.response = requests.put(
            f'http://167.172.172.115:52355/meme/{id_dict['id']}',
            json=payloads.updated_payload,
            headers=headers.default_header
        )
        self.data = self.response.json()
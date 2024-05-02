import requests
from test_data import payloads, headers
from endpoints.base_endpoint import BaseEndpoint
from endpoints.json_schemas import DefaultData

class UpdateMeme(BaseEndpoint):
    def update_meme(self, id_dict, payload=None):
        headers.default_header.update(self.token)
        payload = payload if payload else payloads.updated_payload
        payload.update(id_dict)

        self.response = requests.put(
            f'http://167.172.172.115:52355/meme/{id_dict['id']}',
            json=payload,
            headers=headers.default_header
        )
        if self.response.status_code == 200:
            self.data = DefaultData(**self.response.json())

    def check_updated_tags(self):
        assert self.data.tags == payloads.updated_payload['tags']

    def check_updated_info(self):
        assert self.data.info == payloads.updated_payload['info']
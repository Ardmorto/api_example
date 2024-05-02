import requests
from test_data import headers, payloads
from endpoints.base_endpoint import BaseEndpoint
from endpoints.json_schemas import DefaultData

class MemeById(BaseEndpoint):

    def get_meme_by_id(self, id_dict):
        headers.default_header.update(self.token)
        self.response = requests.get(
            f'http://167.172.172.115:52355/meme/{id_dict['id']}',
            headers=headers.default_header
        )
        if self.response.status_code == 200:
            self.data = DefaultData(**self.response.json())

    def check_id_is_correct(self, id):
        assert self.data.id == id

    def check_username_is_correct(self):
        assert self.data.updated_by == payloads.credentials['name']
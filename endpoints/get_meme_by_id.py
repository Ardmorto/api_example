import requests
from test_data import headers
from endpoints.base_endpoint import BaseEndpoint

class MemeById(BaseEndpoint):

    def get_meme_by_id(self, id_dict):
        headers.default_header.update(self.token)
        self.response = requests.get(
            f'http://167.172.172.115:52355/meme/{id_dict['id']}',
            headers=headers.default_header
        )
        self.data = self.response.json()

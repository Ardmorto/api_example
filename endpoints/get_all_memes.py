import requests
from test_data import headers
from endpoints.base_endpoint import BaseEndpoint

class GetAllMemes(BaseEndpoint):

    def get_all_memes(self):
        headers.default_header.update(self.token)
        self.response = requests.get(
            'http://167.172.172.115:52355/meme',
            headers=headers.default_header
        )
        self.data = self.response.json()

    def count_memes_check(self):
        assert len(self.data['data']) > 10
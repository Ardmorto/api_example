import requests


class CheckToken():
    def check_token_is_alive(self, token):
        self.response = requests.get(f'http://167.172.172.115:52355/authorize/{token}')
        return self.response.status_code == 200

    def check_response_is_200(self):
        assert self.response.status_code == 200
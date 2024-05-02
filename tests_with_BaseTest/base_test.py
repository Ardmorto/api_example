import requests
from test_data import payloads, headers
from endpoints.json_schemas import AuthData
from endpoints.authorize import Authorize
from endpoints.check_token import CheckToken
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_meme_by_id import MemeById
from endpoints.add_new_meme import AddMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme

class BaseTest:
    def setup_method(self):
        self.authorization_endp = Authorize()
        self.check_token_endp = CheckToken()
        self.all_memes_endp = GetAllMemes(self.get_token())
        self.meme_by_id_endp = MemeById(self.get_token())
        self.add_meme_endp = AddMeme(self.get_token())
        self.meme_upd_endp = UpdateMeme(self.get_token())
        self.delete_meme_endp = DeleteMeme(self.get_token())

    def get_token(self):
        self.response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=payloads.credentials,
            headers=headers.default_header
        )
        if self.response.status_code == 200:
            self.data = AuthData(**self.response.json())
        return {'Authorization': self.data.token}

import pytest
import os
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_meme_by_id import MemeById
from endpoints.add_new_meme import AddMeme
from endpoints.update_meme import UpdateMeme
from endpoints.authorize import Authorize
from endpoints.check_token import CheckToken
from endpoints.delete_meme import DeleteMeme

@pytest.fixture()
def authorization(check_token_endp, authorization_endp):
    token = os.getenv('MEME_API_TOKEN')
    if token and check_token_endp.check_token_is_alive(token):
        pass
    else:
        os.environ['MEME_API_TOKEN'] = authorization_endp.get_token()
        token = os.getenv('MEME_API_TOKEN')
    token_dict = {'Authorization': token}
    return token_dict

@pytest.fixture
def new_meme(add_meme_endp, delete_meme_endp):
    add_meme_endp.add_new_meme()
    id = add_meme_endp.data.id
    yield {'id': id}
    delete_meme_endp.delete_meme(id)

@pytest.fixture
def new_meme_without_deletion(add_meme_endp):
    add_meme_endp.add_new_meme()
    id = add_meme_endp.data.id
    yield {'id': id}

@pytest.fixture()
def authorization_endp():
    return Authorize()

@pytest.fixture()
def check_token_endp():
    return CheckToken()

@pytest.fixture()
def all_memes_endp(authorization):
    return GetAllMemes(authorization)

@pytest.fixture()
def meme_by_id_endp(authorization):
    return MemeById(authorization)

@pytest.fixture()
def add_meme_endp(authorization):
    return AddMeme(authorization)

@pytest.fixture()
def meme_upd_endp(authorization):
    return UpdateMeme(authorization)

@pytest.fixture()
def delete_meme_endp(authorization):
    return DeleteMeme(authorization)
import pytest
import requests
import os
from test_data import payloads, headers
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_meme_by_id import MemeById
from endpoints.add_new_meme import AddMeme
from endpoints.update_meme import UpdateMeme

@pytest.fixture(scope='session')
def authorization():
    token = os.getenv('MEME_API_TOKEN')
    if not token:
        response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=payloads.credentials,
            headers=headers.default_header
        )
        token = response.json()['token']
        os.environ['MEME_API_TOKEN'] = token
    return {'Authorization': token}

@pytest.fixture
def new_meme(authorization):
    headers.default_header.update(authorization)
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        json=payloads.default_payload,
        headers=headers.default_header
    )
    id = response.json()['id']
    yield {'id': id}
    requests.delete(
        f'http://167.172.172.115:52355/meme/{id}',
        headers=headers.default_header
    )

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
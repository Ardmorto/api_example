import pytest
import requests
from test_data import payloads, headers
from endpoints.get_all_memes import GetAllMemes
from endpoints.get_meme_by_id import MemeById
@pytest.fixture(scope='session')
def authorization():
    response = requests.post(
        'http://167.172.172.115:52355/authorize',
        json=payloads.credentials,
        headers=headers.default_header
    )
    token = response.json()['token']
    return {'Authorization': token}

@pytest.fixture
def new_meme(authorization):
    headers.default_header.update(authorization)
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        json=payloads.new_meme_payload,
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
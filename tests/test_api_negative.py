import requests
from test_data import payloads, headers


def test_add_new_meme_negative(authorization):
    headers.default_header.update(authorization)
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        json=payloads.new_meme_without_url,
        headers=headers.default_header
    )
    assert response.status_code == 400
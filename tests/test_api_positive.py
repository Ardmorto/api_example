import requests
from test_data import payloads, headers

def test_token_alive(authorization):
    response = requests.get(f'http://167.172.172.115:52355/authorize/{authorization['Authorization']}')
    assert response.status_code == 200

def test_get_all_memes(all_memes_endp):
    all_memes_endp.get_all_memes()
    all_memes_endp.check_response_is_200()
    all_memes_endp.count_memes_check()

def test_get_meme_by_id(meme_by_id_endp, new_meme):
    meme_by_id_endp.get_meme_by_id(new_meme['id'])
    meme_by_id_endp.check_response_is_200()

def test_add_new_meme(authorization):
    headers.default_header.update(authorization)
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        json=payloads.new_meme_payload,
        headers=headers.default_header
    )
    assert response.status_code == 200

def test_change_meme(authorization, new_meme):
    headers.default_header.update(authorization)
    payloads.new_meme_payload.update(new_meme)
    response = requests.put(
        f'http://167.172.172.115:52355/meme/{new_meme['id']}',
        json=payloads.new_meme_payload,
        headers=headers.default_header
    )
    assert response.status_code == 200
import requests

def test_token_alive(authorization):
    response = requests.get(f'http://167.172.172.115:52355/authorize/{authorization['Authorization']}')
    assert response.status_code == 200

def test_get_all_memes(all_memes_endp):
    all_memes_endp.get_all_memes()
    all_memes_endp.check_response_is_200()
    all_memes_endp.count_memes_check()

def test_get_meme_by_id(meme_by_id_endp, new_meme):
    meme_by_id_endp.get_meme_by_id(new_meme)
    meme_by_id_endp.check_response_is_200()

def test_add_new_meme(add_meme_endp):
    add_meme_endp.add_new_meme()
    add_meme_endp.check_response_is_200()

def test_update_meme(meme_upd_endp, new_meme):
    meme_upd_endp.update_meme(new_meme)
    meme_upd_endp.check_response_is_200()
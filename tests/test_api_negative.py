from test_data import payloads


def test_add_new_meme_negative(add_meme_endp):
    add_meme_endp.add_new_meme(payload=payloads.payload_without_url)
    add_meme_endp.check_response_is_400()

def test_update_meme_negative(meme_upd_endp, new_meme):
    meme_upd_endp.update_meme(new_meme, payload=payloads.payload_without_url)
    meme_upd_endp.check_response_is_400()
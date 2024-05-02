def test_authorization(authorization_endp):
    authorization_endp.get_token()
    authorization_endp.check_response_is_200()
    authorization_endp.check_username()

def test_cheking_token(authorization, check_token_endp):
    check_token_endp.check_token_is_alive(authorization['Authorization'])
    check_token_endp.check_response_is_200()

def test_get_all_memes(all_memes_endp):
    all_memes_endp.get_all_memes()
    all_memes_endp.check_response_is_200()
    all_memes_endp.count_memes_check()

def test_get_meme_by_id(meme_by_id_endp, new_meme):
    meme_by_id_endp.get_meme_by_id(new_meme)
    meme_by_id_endp.check_response_is_200()
    meme_by_id_endp.check_id_is_correct(new_meme['id'])
    meme_by_id_endp.check_username_is_correct()

def test_add_new_meme(add_meme_endp):
    add_meme_endp.add_new_meme()
    add_meme_endp.check_response_is_200()
    add_meme_endp.check_id_assigned()
    add_meme_endp.check_username_is_correct()

def test_update_meme(meme_upd_endp, new_meme):
    meme_upd_endp.update_meme(new_meme)
    meme_upd_endp.check_response_is_200()
    meme_upd_endp.check_updated_tags()
    meme_upd_endp.check_updated_info()

def test_meme_deletion(delete_meme_endp, new_meme_without_deletion):
    delete_meme_endp.delete_meme(new_meme_without_deletion['id'])
    delete_meme_endp.check_response_is_200()
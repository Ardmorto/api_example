from tests_with_BaseTest.base_test import BaseTest
from test_data import payloads

class TestPositive(BaseTest):
    def test_authorization(self):
        self.authorization_endp.get_token()
        self.authorization_endp.check_response_is_200()
        self.authorization_endp.check_username()

    def test_cheking_token(self, authorization):
        self.check_token_endp.check_token_is_alive(authorization['Authorization'])
        self.check_token_endp.check_response_is_200()

    def test_get_all_memes(self):
        self.all_memes_endp.get_all_memes()
        self.all_memes_endp.check_response_is_200()
        self.all_memes_endp.count_memes_check()

    def test_get_meme_by_id(self, new_meme):
        self.meme_by_id_endp.get_meme_by_id(new_meme)
        self.meme_by_id_endp.check_response_is_200()
        self.meme_by_id_endp.check_id_is_correct(new_meme['id'])
        self.meme_by_id_endp.check_username_is_correct()

    def test_add_new_meme(self):
        self.add_meme_endp.add_new_meme()
        self.add_meme_endp.check_response_is_200()
        self.add_meme_endp.check_id_assigned()
        self.add_meme_endp.check_username_is_correct()

    def test_update_meme(self, new_meme):
        self.meme_upd_endp.update_meme(new_meme)
        self.meme_upd_endp.check_response_is_200()
        self.meme_upd_endp.check_updated_tags()
        self.meme_upd_endp.check_updated_info()

    def test_meme_deletion(self, new_meme_without_deletion):
        self.delete_meme_endp.delete_meme(new_meme_without_deletion['id'])
        self.delete_meme_endp.check_response_is_200()

class TestNegative(BaseTest):
    def test_add_new_meme_negative(self):
        self.add_meme_endp.add_new_meme(payload=payloads.payload_without_url)
        self.add_meme_endp.check_response_is_400()

    def test_update_meme_negative(self, new_meme):
        self.meme_upd_endp.update_meme(new_meme, payload=payloads.payload_without_url)
        self.meme_upd_endp.check_response_is_400()
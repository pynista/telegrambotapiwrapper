import unittest
from telegrambotapiwrapper.api.types import *
from telegrambotapiwrapper.response import to_api_type, dataclass_fields_to_d

class TestToApiTypeFunction(unittest.TestCase):
    """Тестирование работы функции to_api_type."""




    def test_to_user(self):
        user1 = User(
            id=1234566,
            is_bot=False,
            first_name="John",
            last_name="Doe",
            username="hdvjkdcjkf123sdbvmdjfvn",
            language_code='ru'
        )

        user2 = User(
            id=1234566,
            is_bot=False,
            first_name="John",
        )

        user3 = User(
            id=1234566,
            is_bot=False,
            first_name="John",
            language_code='en'
        )
        for user_obj in [user1, user2, user3]:
            g_type = to_api_type(dataclass_fields_to_d(user_obj._fields_items), "User")
            self.assertEqual(g_type, user_obj)


    def test_to_chat(self):
        # 1
        chat_photo = ChatPhoto(small_file_id='1fdf235643', big_file_id='3454sdfds56546')
        chat1_with_chat_photo = Chat(
            id=123,
            type='group',
            title='dsdvfvdvxfve',
            all_members_are_administrators=True,
            photo=chat_photo
        )
        to_convert = chat1_with_chat_photo._fields_items

        a = to_api_type(dataclass_fields_to_d(to_convert), tp='Chat')
        b = chat1_with_chat_photo
        print(a)

        self.assertEqual(a, b)






class TestResponse(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.existing_chats = [1234567898765,
                              1111111111111,
                              2222222222222,
                              3333333333333,
                              4444444444444]
        cls.not_existing_chats = [
                              9999999999999,
                              8888888888888,
                              7777777777777,
                              6666666666666,
                              5555555555555]
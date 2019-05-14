import unittest
from telegrambotapiwrapper.utils import is_str_int_float_bool
from telegrambotapiwrapper.utils import is_ends_with_underscore


class TestUtils(unittest.TestCase):

    def test_is_str_int_float_bool(self):
        self.assertTrue(is_str_int_float_bool("assaads"))
        self.assertTrue(is_str_int_float_bool(123))
        self.assertTrue(is_str_int_float_bool(23432.45435))
        self.assertTrue(is_str_int_float_bool(True))

        class A:
            pass
        self.assertFalse(is_str_int_float_bool(A()))

    def test_is_ends_with_underscore(self):
        self.assertTrue(is_ends_with_underscore("asedsaads_"))
        self.assertTrue(is_ends_with_underscore("_aessaads_"))
        self.assertFalse(is_ends_with_underscore("_aseswsdwc"))
        self.assertFalse(is_ends_with_underscore(""))

import unittest

from simplecomiler.io.stream import string_is
from simplecomiler.lexer.lexer import StringHandler, String


class StringTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.handler = StringHandler()

    def test_simple_string(self):
        stream = string_is('"Some Text is here"')

        self.assertTrue(self.handler.can_handle(stream))
        r = self.handler.handle(stream)
        self.assertTrue(isinstance(r, String))
        self.assertEqual(r.value, 'Some Text is here')

    def test_not_enclosed_string(self):
        stream = string_is('"Some Text is here')

        self.assertTrue(self.handler.can_handle(stream))

        with self.assertRaises(Exception) as cm:
            self.handler.handle(stream)

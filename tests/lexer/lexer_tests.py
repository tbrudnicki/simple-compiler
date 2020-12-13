import unittest

from simplecomiler.io.stream import string_is
from simplecomiler.lexer.lexer import NumberHandler


class LexerTest(unittest.TestCase):

    def test_can_handle_positive_numbers(self):
        handler = NumberHandler()
        stream = string_is('1234.239')

        self.assertTrue(handler.can_handle(stream))

    def test_can_handle_negative_numbers(self):
        handler = NumberHandler()
        stream = string_is('-5234.239')

        self.assertTrue(handler.can_handle(stream))


if __name__ == '__main__':
    unittest.main()

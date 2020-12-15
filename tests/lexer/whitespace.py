import unittest

from simplecomiler.io.stream import string_is
from simplecomiler.lexer.lexer import WhitespaceHandler


class WhitespaceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.handler = WhitespaceHandler()

    def test_properly_moves_stream_position_to_nonwhite_character(self):
        stream = string_is('    \t\t   \t W')

        self.assertTrue(self.handler.can_handle(stream))
        self.handler.handle(stream)
        self.assertEqual('W', stream.peek())

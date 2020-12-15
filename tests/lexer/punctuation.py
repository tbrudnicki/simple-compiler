import unittest

from simplecomiler.io.stream import string_is
from simplecomiler.lexer.lexer import PunctuationHandler, Punctuation


class PunctuationTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = PunctuationHandler()

    def test_colon(self):
        stream = string_is(':')

        self.assertTrue(self.handler.can_handle(stream))
        result = self.handler.handle(stream)

        self.assertTrue(isinstance(result, Punctuation))
        self.assertEqual(result.value, ':')

    def test_coma(self):
        stream = string_is(',')

        self.assertTrue(self.handler.can_handle(stream))
        result = self.handler.handle(stream)

        self.assertTrue(isinstance(result, Punctuation))
        self.assertEqual(result.value, ',')

    def test_open_bracket(self):
        stream = string_is('(')

        self.assertTrue(self.handler.can_handle(stream))
        result = self.handler.handle(stream)

        self.assertTrue(isinstance(result, Punctuation))
        self.assertEqual(result.value, '(')

    def test_close_bracket(self):
        stream = string_is(')')

        self.assertTrue(self.handler.can_handle(stream))
        result = self.handler.handle(stream)

        self.assertTrue(isinstance(result, Punctuation))
        self.assertEqual(result.value, ')')

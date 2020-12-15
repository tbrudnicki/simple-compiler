import unittest
from tokenize import Comment

from simplecomiler.io.stream import string_is
from simplecomiler.lexer.lexer import CommentHandler


class CommentHandlerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = CommentHandler()

    def test_comment(self):
        stream = string_is('# This is some comment')

        self.assertTrue(self.handler.can_handle(stream))
        r = self.handler.handle(stream)

        self.assertEqual(r, ' This is some comment')

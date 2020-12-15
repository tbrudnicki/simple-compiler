import unittest

from simplecomiler.io.stream import string_is
from simplecomiler.lexer.lexer import NumberHandler, Number


class NumberHandlerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.number_handler = NumberHandler()

    def test_can_handle_positive_numbers(self):
        stream = string_is('1234.239')

        self.assertTrue(self.number_handler.can_handle(stream))

    def test_can_handle_negative_numbers(self):
        stream = string_is('-5234.239')

        self.assertTrue(self.number_handler.can_handle(stream))

    def test_positive_integer(self):
        stream = string_is('25985')

        self.assertTrue(self.number_handler.can_handle(stream), 'NumberHandler should handle positive integers')
        number = self.number_handler.handle(stream)

        self.assertTrue(isinstance(number, Number))
        self.assertTrue(number.value, '25985')

    def test_negative_integer(self):
        stream = string_is('-43298')
        self.assertTrue(self.number_handler.can_handle(stream), 'NumberHandler should handle negative integers')
        number = self.number_handler.handle(stream)

        self.assertTrue(isinstance(number, Number))
        self.assertTrue(number.value, '-43298')

    def test_positive_float(self):
        stream = string_is('567.9876')
        self.assertTrue(self.number_handler.can_handle(stream), 'NumberHandler should handle positive floats')
        number = self.number_handler.handle(stream)

        self.assertTrue(isinstance(number, Number))
        self.assertTrue(number.value, '567.9876')

    def test_negative_float(self):
        stream = string_is('-9567.9876')
        self.assertTrue(self.number_handler.can_handle(stream), 'NumberHandler should handle positive floats')
        number = self.number_handler.handle(stream)

        self.assertTrue(isinstance(number, Number))
        self.assertTrue(number.value, '-9567.9876')

    def test_positive_scientific_integer(self):
        stream = string_is('25E5')
        number = self.number_handler.handle(stream)

        self.assertTrue(isinstance(number, Number))
        self.assertTrue(number.value, '25E5')

    def test_negative_scientific_integer(self):
        stream = string_is('-2E-5')
        number = self.number_handler.handle(stream)

        self.assertTrue(isinstance(number, Number))
        self.assertTrue(number.value, '-2E-5')

    def test_positive_scientific_float(self):
        stream = string_is('2.78E5')
        number = self.number_handler.handle(stream)

        self.assertTrue(isinstance(number, Number))
        self.assertTrue(number.value, '2.78E5')

    def test_negative_scientific_float(self):
        stream = string_is('-2.78E5')
        number = self.number_handler.handle(stream)

        self.assertTrue(isinstance(number, Number))
        self.assertTrue(number.value, '-2.78E5')

    def test_incorrect_scientific_form_throws_exception(self):
        stream = string_is('-2.78Ea')

        with self.assertRaises(Exception) as cm:
            number = self.number_handler.handle(stream)


if __name__ == '__main__':
    unittest.main()

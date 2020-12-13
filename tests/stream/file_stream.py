import unittest
from io import StringIO
from pathlib import Path

from simplecomiler.io.stream import file_is


class FileStreamTestCase(unittest.TestCase):
    TEST_DATA_ROOT = Path(__file__).parent.parent.parent.joinpath('data').joinpath('test')

    def test_retrieve_same_string_as_input(self):
        input_sting = 'some string'
        input_stream = file_is(StringIO(input_sting))
        aggregate = []
        while not input_stream.eof():
            aggregate.append(input_stream.next())

        self.assertEqual(input_sting, ''.join(aggregate), '')

    def test_peek_retrieves_proper_values(self):
        input_sting = 'some string'
        input_stream = string_is(input_sting)
        aggregate = []
        while not input_stream.eof():
            peek_result = input_stream.peek()
            next_result = input_stream.next()
            self.assertEqual(peek_result, next_result, 'peek should return same values as next')

    def test_peek_doesnt_change_stream_position(self):
        input_sting = 'some string'
        input_stream = string_is(input_sting)

        peek1_1 = input_stream.peek()
        peek1_2 = input_stream.peek()
        next_1 = input_stream.next()

        self.assertEqual(peek1_1, peek1_2, 'peeks from same position in the stream should return same value')
        self.assertEqual(peek1_2, next_1, 'peek should return same values as next')

        peek2_1 = input_stream.peek()
        peek2_2 = input_stream.peek()
        next_2 = input_stream.next()

        self.assertEqual(peek2_1, peek2_2, 'peeks from same position in the stream should return same value')
        self.assertEqual(peek2_2, next_2, 'peek should return same values as next')


    @staticmethod
    def data_file(file_name):
        return FileStreamTestCase.TEST_DATA_ROOT.joinpath(file_name)


if __name__ == '__main__':
    unittest.main()

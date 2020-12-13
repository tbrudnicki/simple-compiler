import unittest

from simplecomiler.io.stream import string_is


class StringStreamTestCase(unittest.TestCase):
    def test_consume_all_stream_gives_same_string(self):
        input_sting = 'some string'
        input_stream = string_is(input_sting)
        aggregate = []
        while not input_stream.eof():
            aggregate.append(input_stream.next())

        self.assertEqual(input_sting, ''.join(aggregate), '')

    def test_peek_returns_same_values_as_next(self):
        input_sting = 'some string'
        input_stream = string_is(input_sting)
        aggregate = []
        while not input_stream.eof():
            peek_result = input_stream.peek()
            next_result = input_stream.next()
            self.assertEqual(peek_result, next_result, 'peek should return same values as next')

    def test_peek_does_not_change_stream_position(self):
        input_sting = 'some string'
        input_stream = string_is(input_sting)

        position_1 = input_stream.current_position()

        peek1_1 = input_stream.peek()
        peek1_2 = input_stream.peek()

        self.assertEqual(position_1, input_stream.current_position(), 'peek should not change position in the stream')
        self.assertEqual(peek1_1, peek1_2, 'peeks from same position in the stream should return same value')

        next_1 = input_stream.next()
        after_next_position = input_stream.current_position()
        self.assertNotEqual(position_1, after_next_position, 'next should change position in the stream')
        self.assertEqual(position_1.line, after_next_position.line, 'line should remain the same')
        self.assertEqual(position_1.col + 1, after_next_position.col, 'next should increase col + 1')

        self.assertEqual(peek1_2, next_1, 'peek should return same values as next')

        peek2_1 = input_stream.peek()
        peek2_2 = input_stream.peek()
        next_2 = input_stream.next()

        self.assertEqual(peek2_1, peek2_2, 'peeks from same position in the stream should return same value')
        self.assertEqual(peek2_2, next_2, 'peek should return same values as next')

    def test_next_properly_updates_stream_position(self):
        input_sting = 'some string\n \nsome'
        input_stream = string_is(input_sting)

        position_1 = input_stream.current_position()
        self.assertEqual(position_1.col, 0)
        self.assertEqual(position_1.line, 1)

        for i in range(0, 12):
            print(input_stream.next())

        position_2 = input_stream.current_position()

        self.assertEqual(0, position_2.col)
        self.assertEqual(2, position_2.line)

        while not input_stream.eof():
            input_stream.next()

        position_3 = input_stream.current_position()
        self.assertEqual(position_3.line, 3)
        self.assertEqual(position_3.col, 4)


if __name__ == '__main__':
    unittest.main()

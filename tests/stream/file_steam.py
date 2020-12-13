import unittest
from pathlib import Path


class FileStreamTestCase(unittest.TestCase):

    def test_simple(self):
        print(Path(__file__).parent.parent.parent.joinpath('data').joinpath('test'))


if __name__ == '__main__':
    unittest.main()

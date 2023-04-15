import unittest

from generator import *


class TestGenerator(unittest.TestCase):
    def test_whenTypical(self):
        generator = Generator()
        actual = generator._new_empty_tile()
        expected = """⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""
        self.assertTrue(expected == actual)


if __name__ == "__main__":
    unittest.main()

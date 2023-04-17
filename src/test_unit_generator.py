import unittest

from generator import *


class TestGenerator(unittest.TestCase):
    def test_whenTypical(self):
        expected = """⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""

        generator = Generator()
        actual = generator._Generator__new_empty_tile()

        self.assertTrue(expected == actual)

    def test_insert_4pixels_works_whenEmpty(self):
        generator = Generator()
        tile = generator._Generator__new_empty_tile()
        rows = tile.split("\n")

        can_insert = generator._Generator__insert_pixels(rows, 2, 2)

        self.assertTrue(can_insert)

    def test_insert_4pixels_works_whenRight(self):
        tile = """⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""

        expected = """⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕🔵🔵⭕⭕⭕⭕⭕
⭕🔵🔵⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""

        generator = Generator()
        rows = tile.split("\n")

        can_insert = generator._Generator__insert_pixels(rows, 2, 2)

        self.assertTrue(can_insert)

    # @unittest.skip
    def test_debug(self):
        g = Generator(initial_tiles=[])
        g.run()


if __name__ == "__main__":
    unittest.main()

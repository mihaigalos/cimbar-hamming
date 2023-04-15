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
        actual = generator._new_empty_tile()

        self.assertTrue(expected == actual)

    def test_validate_pixel_works_whenEmpty(self):
        generator = Generator()
        tile = generator._new_empty_tile()
        rows = tile.split("\n")

        can_insert = generator._validate_pixel(rows, 2, 2)

        self.assertTrue(can_insert)

    def test_validate_pixel_works_whenRight(self):
        tile = """⭕⭕⭕⭕⭕⭕⭕⭕
🔵🔵🔵⭕⭕⭕⭕⭕
🔵🔵⭕⭕⭕⭕⭕⭕
🔵🔵🔵⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""

        generator = Generator()
        rows = tile.split("\n")

        can_insert = generator._validate_pixel(rows, 2, 2)

        self.assertTrue(can_insert)

    def test_validate_pixel_works_whenLeft(self):
        tile = """⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕🔵🔵🔵⭕⭕⭕
⭕⭕⭕🔵🔵⭕⭕⭕
⭕⭕🔵🔵🔵⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""

        generator = Generator()
        rows = tile.split("\n")

        can_insert = generator._validate_pixel(rows, 2, 2)

        self.assertTrue(can_insert)

    def test_validate_pixel_works_whenDown(self):
        tile = """⭕⭕⭕⭕⭕⭕⭕⭕
⭕🔵🔵🔵⭕⭕⭕⭕
⭕🔵⭕🔵⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""

        generator = Generator()
        rows = tile.split("\n")

        can_insert = generator._validate_pixel(rows, 2, 2)

        self.assertTrue(can_insert)

    def test_validate_pixel_works_whenUp(self):
        tile = """⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕🔵⭕🔵⭕⭕⭕⭕
⭕🔵🔵🔵⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""

        generator = Generator()
        rows = tile.split("\n")

        can_insert = generator._validate_pixel(rows, 2, 2)

        self.assertTrue(can_insert)

    def test_validate_pixel_not_works_whenBitSet(self):
        tile = """⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕🔵🔵🔵⭕⭕⭕⭕
⭕🔵🔵🔵⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""

        generator = Generator()
        rows = tile.split("\n")

        can_insert = generator._validate_pixel(rows, 2, 2)

        self.assertFalse(can_insert)


if __name__ == "__main__":
    unittest.main()

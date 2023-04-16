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

    def test_validate_pixel_works_whenEmpty(self):
        generator = Generator()
        tile = generator._Generator__new_empty_tile()
        rows = tile.split("\n")

        can_insert = generator._Generator__validate_pixel(rows, 2, 2)

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

        can_insert = generator._Generator__validate_pixel(rows, 2, 2)

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

        can_insert = generator._Generator__validate_pixel(rows, 2, 2)

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

        can_insert = generator._Generator__validate_pixel(rows, 2, 2)

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

        can_insert = generator._Generator__validate_pixel(rows, 2, 2)

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

        can_insert = generator._Generator__validate_pixel(rows, 2, 2)

        self.assertFalse(can_insert)

    def test_create_potential_tile_works_whenRight(self):
        tile = """⭕⭕⭕⭕⭕⭕⭕⭕
🔵🔵🔵⭕⭕⭕⭕⭕
🔵🔵⭕⭕⭕⭕⭕⭕
🔵🔵🔵⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""
        expected = """⭕⭕⭕⭕⭕⭕⭕⭕
🔵🔵🔵⭕⭕⭕⭕⭕
🔵🔵🔵⭕⭕⭕⭕⭕
🔵🔵🔵⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕"""
        generator = Generator()

        actual = generator._Generator__create_potential_tile(2, 2, tile)

        self.assertTrue(actual, expected)


if __name__ == "__main__":
    unittest.main()

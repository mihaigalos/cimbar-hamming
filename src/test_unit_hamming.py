import unittest

from hamming import Hamming


class TestGenerator(unittest.TestCase):
    def test_hamming_works_whenTypical(self):
        expected_min_max = (18, 60)

        sut = Hamming()
        sut.compute_distances()
        actual_min_max = (sut.min_hamming_distance, sut.max_hamming_distance)

        self.assertTrue(expected_min_max == actual_min_max)

    def test_hamming_works_whenTypical2(self):
        expected_min_max = (16, 16)
        initial_tiles = ["""🔵⭕⭕⭕⭕⭕⭕⭕
🔵⭕⭕⭕⭕⭕⭕⭕
🔵⭕⭕⭕⭕⭕⭕⭕
🔵⭕⭕⭕⭕⭕⭕⭕
🔵⭕⭕⭕⭕⭕⭕⭕
🔵⭕⭕⭕⭕⭕⭕⭕
🔵⭕⭕⭕⭕⭕⭕⭕
🔵⭕⭕⭕⭕⭕⭕⭕
""",
                         """⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕⭕⭕
⭕⭕⭕⭕⭕⭕🔵🔵
⭕⭕⭕⭕⭕🔵🔵🔵
⭕⭕⭕⭕⭕⭕🔵🔵
⭕⭕⭕⭕⭕⭕⭕🔵
"""]

        sut = Hamming(initial_tiles)
        sut.compute_distances()
        actual_min_max = (sut.min_hamming_distance, sut.max_hamming_distance)

        self.assertTrue(expected_min_max == actual_min_max)


if __name__ == "__main__":
    unittest.main()

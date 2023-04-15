import random

from default_tiles import *
from hamming import Hamming

from writer import Writer


class Generator:
    def __init__(self, tile_size=8, initial_tiles=DEFAULT_TILES, desired_tile_count=64):
        self.desired_tile_count = desired_tile_count
        self.initial_tiles = initial_tiles
        self.threshold_for_hamming = 20
        self.threshold_max_iterations = 1000000
        self.threshold_min_written_pixels = 5
        self.tile_index = len(initial_tiles) + 1
        self.tile_size = tile_size
        self.writer = Writer("results")

    def run(self):
        all_tiles = self.initial_tiles

        while len(all_tiles) < self.desired_tile_count:
            print(
                f"----------------- Searching for tile {len(all_tiles+1)} -----------------")
            newtile = self._generate_tile(all_tiles)
            all_tiles.append(newtile)

    # def _generate_tile(self, all_tiles):
    #     written_pixels = 0
    #     iteration = 0
    #     while self._continue_generating(written_pixels, iteration):
    #         new_pixel_x = random.randint(0, self.tile_size - 1)
    #         new_pixel_y = random.randint(0, self.tile_size - 1)
    #         potential_tile = self._create_potential_tile(
    #             new_pixel_x, new_pixel_y)
    #         if potential_tile is not None:
    #             if written_pixels >= self.threshold_min_written_pixels:
    #                 hamming = Hamming(all_tiles)
    #                 if hamming >= self.threshold_for_hamming:
    #                     return tile

    #     return None

    # def _create_potential_tile(self, new_pixel_x, new_pixel_y, old_tile):
    #     rows = old_tile.split("\n")
    #     if self._validate_pixel(rows, new_pixel_x, new_pixel_y):
    #         rows[new_pixel_y][new_pixel_x] = "🔵"
    #         return rows.join("\n")

    # def _validate_pixel(self, rows, new_pixel_x, new_pixel_y):
    #     result = rows[new_pixel_y][new_pixel_x] == "⭕"
    #     if new_pixel_

    def _new_empty_tile(self):
        result = ""
        for row in range(0, self.tile_size):
            result += "⭕"*self.tile_size
            if row < self.tile_size - 1:
                result += "\n"
        return result

    def _continue_generating(self, written_pixels, iteration):
        return written_pixels < int(self.tile_size*self.tile_size * 3.0 / 4.0) and iteration < self.threshold_max_iterations

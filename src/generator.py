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
        iteration = 0

        while len(all_tiles) < self.desired_tile_count and self._can_continue_creating_potential_tiles(iteration):
            print(
                f"----------------- Searching for tile {len(all_tiles) + 1} -----------------")
            newtile = self._generate_tile(all_tiles)
            if newtile is not None:
                print(newtile)
                all_tiles.append(newtile)
            iteration += 1

    def _generate_tile(self, all_tiles):
        written_pixels = 0
        iteration = 0
        tile = self._new_empty_tile()
        while self._can_continue_generating_pixels(written_pixels):
            new_pixel_x = random.randint(0, self.tile_size - 1)
            new_pixel_y = random.randint(0, self.tile_size - 1)
            potential_tile = self._create_potential_tile(
                new_pixel_x, new_pixel_y, tile)
            if potential_tile is not None:
                if written_pixels >= self.threshold_min_written_pixels:
                    hamming = Hamming(all_tiles)
                    if hamming >= self.threshold_for_hamming:
                        return tile
                written_pixels += 1

        return None

    def _create_potential_tile(self, new_pixel_x, new_pixel_y, old_tile):
        rows = old_tile.split("\n")
        if self._validate_pixel(rows, new_pixel_x, new_pixel_y):
            #rows[new_pixel_y][new_pixel_x] = "🔵"
            row = rows[new_pixel_y]
            new_row = row[0:new_pixel_x] + "🔵" + row[new_pixel_x:len(row)]
            if new_pixel_y < self.tile_size-1:
                new_row += "\n"
            new_rows = rows[0:new_pixel_y] + \
                [new_row] + rows[new_pixel_y:len(rows)]

            return new_rows
        return None

    """
    Coordinate system: X - Left to Right, Y: Top to Bottom
    """

    def _validate_pixel(self, rows, new_pixel_x, new_pixel_y):
        if self._is_empty_tile(rows):
            return True

        if rows[new_pixel_y][new_pixel_x] == "⭕" and (
            (new_pixel_x - 1 > 0 and rows[new_pixel_y][new_pixel_x - 1] == "🔵") or
            (new_pixel_y - 1 > 0 and rows[new_pixel_y - 1][new_pixel_x] == "🔵") or
            (new_pixel_x + 1 < self.tile_size and rows[new_pixel_y][new_pixel_x + 1] == "🔵") or
            (new_pixel_y + 1 <
             self.tile_size and rows[new_pixel_y + 1][new_pixel_x] == "🔵")
        ):
            return True
        return False

    def _is_empty_tile(self, rows):
        for row in rows:
            if "🔵" in row:
                return False
        return True

    def _new_empty_tile(self):
        result = ""
        for row in range(0, self.tile_size):
            result += "⭕"*self.tile_size
            if row < self.tile_size - 1:
                result += "\n"
        return result

    def _can_continue_generating_pixels(self, written_pixels):
        return written_pixels < int(self.tile_size*self.tile_size * 3.0 / 4.0)

    def _can_continue_creating_potential_tiles(self, iteration):
        return iteration < self.threshold_max_iterations

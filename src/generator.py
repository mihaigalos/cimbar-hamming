import random

from default_tiles import *
from hamming import Hamming

from writer import Writer


class Generator:
    def __init__(self, initial_tiles=DEFAULT_TILES, tile_size=5, desired_tile_count=16):
        self.desired_tile_count = desired_tile_count
        self.initial_tiles = initial_tiles
        self.threshold_for_hamming = 10
        self.threshold_max_epochs = 1000
        self.threshold_max_generations_per_epoch = 10000
        self.threshold_max_add_pixel_iterations_per_generation = 10000
        self.threshold_min_written_pixels = 7
        self.tile_index = len(initial_tiles) + 1
        self.tile_size = tile_size
        self.writer = Writer("results")

    def run(self):
        epoch = 0
        condition = True
        while condition:
            initial_tiles = self.initial_tiles.copy()
            print(
                f"+++++++++++++++++ Epoch {epoch} +++++++++++++++++")
            new_tiles = self.__epoch_loop(initial_tiles)
            condition = self.__can_continue_epochs(new_tiles, epoch)
            epoch += 1

    def __epoch_loop(self, initial_tiles):
        all_tiles = initial_tiles.copy()
        iteration = 0
        while self.__can_continue_generation(len(all_tiles), iteration):
            newtile = self.__generation_loop(all_tiles)
            if newtile is not None:
                print(
                    f"----------------- Searching for tile {len(all_tiles) + 1} -----------------")
                print(f"{newtile}")
                all_tiles.append(newtile)
            iteration += 1
        return all_tiles

    def __generation_loop(self, all_tiles):
        written_pixels = 1
        tile = self.__new_empty_tile()
        iteration = 0
        while self.__can_continue_generating_pixels(written_pixels, iteration):
            new_pixel_x = random.randint(1, self.tile_size - 1)
            new_pixel_y = random.randint(1, self.tile_size - 1)

            potential_tile = self.__create_potential_tile(
                new_pixel_x, new_pixel_y, tile)
            if potential_tile is not None:
                tile = potential_tile
                if written_pixels >= self.threshold_min_written_pixels:
                    new_tiles = all_tiles.copy()
                    new_tiles.append(potential_tile)
                    hamming = Hamming(new_tiles)
                    hamming.compute_distances()
                    if hamming.min_hamming_distance >= self.threshold_for_hamming:
                        return tile
                written_pixels += 1
            iteration += 1

        return None

    def __create_potential_tile(self, new_pixel_x, new_pixel_y, old_tile):
        rows = old_tile.strip().split("\n")
        (validated, new_rows) = self.__insert_pixels(
            rows, new_pixel_x, new_pixel_y)

        if validated:
            result = "\n".join(new_rows).strip()+"\n"
            return result

        return None

    """
    Coordinate system: X - Left to Right, Y: Top to Bottom
    We're using 4 pixels here to assist in decoding and compensate for camera blur.
    """

    def __insert_pixels(self, rows, new_pixel_x, new_pixel_y):

        if self.__is_empty_tile(rows) or (
                rows[new_pixel_y][new_pixel_x] == "⭕" and (
                    (new_pixel_x - 1 > 0 and rows[new_pixel_y][new_pixel_x - 1] == "🔵") or
                    (new_pixel_y - 1 > 0 and rows[new_pixel_y - 1][new_pixel_x] == "🔵") or
                    (new_pixel_x + 1 < self.tile_size and rows[new_pixel_y][new_pixel_x + 1] == "🔵") or
                    (new_pixel_y + 1 <
                     self.tile_size and rows[new_pixel_y + 1][new_pixel_x] == "🔵")
                )):
            rows[new_pixel_y] = self.__mutate_string(
                rows[new_pixel_y], new_pixel_x, "🔵")
            added_pixels = 0
            next_x = 0
            next_y = 0
            return (True, rows)
        return (False, rows)

    def __mutate_string(self, input, pos, newchar):
        l = list(input)
        l[pos] = newchar
        return "".join(l)

    def __is_empty_tile(self, rows):
        for row in rows:
            if "🔵" in row:
                return False
        return True

    def __new_empty_tile(self):
        result = ""
        for row in range(0, self.tile_size):
            result += "⭕"*self.tile_size
            if row < self.tile_size - 1:
                result += "\n"
        return result

    def __can_continue_generating_pixels(self, written_pixels, iteration):
        return written_pixels < int(self.tile_size*self.tile_size * 3.0 / 4.0) and iteration < self.threshold_max_add_pixel_iterations_per_generation

    def __can_continue_generation(self, len_all_tiles, iteration):
        return len_all_tiles < self.desired_tile_count and iteration < self.threshold_max_generations_per_epoch

    def __can_continue_epochs(self, new_tiles, epoch):
        return new_tiles is None or (len(new_tiles) < self.desired_tile_count and epoch < self.threshold_max_epochs)

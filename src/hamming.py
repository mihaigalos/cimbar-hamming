import json
import math

from default_tiles import DEFAULT_TILES


class Hamming:

    def __init__(self, default_tiles=DEFAULT_TILES):
        if len(default_tiles) > 0 and default_tiles[0][0] == "\n":
            self.tiles = self._remove_tile_first_newline(default_tiles)
        else:
            self.tiles = default_tiles
        self.min_hamming_distance = 1000000000
        self.max_hamming_distance = 0

    def _remove_tile_first_newline(self, tiles):
        result = []
        for tile in tiles:
            tile = tile[1:]
            result.append(tile)
        return result

    def compute_distances(self):
        hamming_distances = {}
        i = 0
        if len(self.tiles) > 1:
            for tile1 in self.tiles:
                one_distance = {}
                j = 0
                for tile2 in self.tiles:
                    if i != j:
                        one_distance[j] = self._diff_tile(tile1, tile2)
                        if self.max_hamming_distance < one_distance[j]:
                            self.max_hamming_distance = one_distance[j]
                        if self.min_hamming_distance > one_distance[j]:
                            self.min_hamming_distance = one_distance[j]
                    j += 1

                hamming_distances[i] = one_distance
                i += 1
        return hamming_distances

    def to_json(self):
        json_object = json.dumps(self.compute_distances(), indent=4)
        print(json_object)

    def print(self):
        self.to_json()
        print(f"Min Hamming distance: {self.min_hamming_distance}")
        print(f"Max Hamming distance: {self.max_hamming_distance}")

    def _diff_tile(self, tile1, tile2) -> int:
        hamming_distance = 0
        i = -1
        for pixel1 in tile1:
            i = i+1
            if pixel1 == '\n' or pixel1 == '\r':
                continue
            pixel2 = tile2[i]
            if pixel2 == '\n' or pixel2 == '\r':
                continue
            if pixel1 != pixel2:
                hamming_distance += 1
        return hamming_distance

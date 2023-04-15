from default_tiles import *


class Generator:

    def __init__(self):
        self.tile_size = 7  # NxN pixels per tile
        self.tiles = self._remove_tile_first_newline(DEFAULT_TILES)

    def _remove_tile_first_newline(self, tiles):
        result = []
        for tile in tiles:
            tile = tile[1:]
            result.append(tile)
        return result

    def run(self):
        pass


gen = Generator()

print(gen.tiles[9])

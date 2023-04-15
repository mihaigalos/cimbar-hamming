class Hamming:

    def __init__(self, tile_size, default_tiles):
        self.tile_size = tile_size  # NxN pixels per tile
        self.tiles = self._remove_tile_first_newline(default_tiles)

    def _remove_tile_first_newline(self, tiles):
        result = []
        for tile in tiles:
            tile = tile[1:]
            result.append(tile)
        return result

    def run(self):
        pass

from default_tiles import *


class Generator:

    def __init__(self):
        self.pixel_set = "🔵"
        self.pixel_unset = "⭕"
        self.tile_size = 7  # NxN pixels per tile

    def run(self):
        print(self.pixel_set, end="")
        print(self.pixel_set, end="")
        print(self.pixel_set, end="")
        print(self.pixel_set, end="")
        print(self.pixel_unset, end="")
        print(self.pixel_unset, end="")
        print(self.pixel_unset, end="")
        print(self.pixel_unset, end="")


gen = Generator()

print(DEFAULT_TILES[9])

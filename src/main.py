import sys
from generator import Generator
from hamming import Hamming
from default_tiles import *

h = Hamming(DEFAULT_TILE_5x5)
h.compute_distances()
h.print()
# if len(sys.argv) > 1 and sys.argv[1] == "--no-default-tiles":
#     g = Generator(initial_tiles=[])
# else:
#     g = Generator()
# g.run()

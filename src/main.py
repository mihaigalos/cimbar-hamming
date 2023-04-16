import sys
from generator import Generator

if len(sys.argv) > 1 and sys.argv[1] == "--no-default-tiles":
    g = Generator(initial_tiles=[])
else:
    g = Generator()
g.run()

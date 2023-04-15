@default:
    just --list --unsorted

@run:
    python3 src/main.py

@test:
    python -m unittest discover src/
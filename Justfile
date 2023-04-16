@default:
    just --list --unsorted

@run +args="":
    python3 src/main.py {{ args}}

@test:
    python -m unittest discover src/
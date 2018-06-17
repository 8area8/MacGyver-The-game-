#! /usr/bin/env python3
# coding: utf-8

"""List all game's maps."""

import glob
from pathlib import Path


def import_map():
    """Import the map file in a list.

    Only the first file will be imported.
    """
    file = glob.glob(str(Path().resolve() / "assets" / "*.txt"))
    content = []

    with open(file[0]) as f:
        for line in f:
            line.remove("\n")
            content.append(list(line))

    inspect_the_map(content)
    return content


def inspect_the_map(content):
    """Inspect the map.

    Raise a ValueError if the map does not meet the standards.

    Note: the map must have 15 lines of 15 characters.
    Possible Characters are 'O' for walls, ' ' for paths and 'G' for guardian.
    """
    possibles_keys = ('O', ' ', 'G')
    if len(content) == 15:
        if all(len(line) == 15 for line in content):
            if all(key in possibles_keys for line in content for key in line):
                return

    raise ValueError("Invalide map: the map must have "
                     "15 lines of 15 characters."
                     "Possible Characters: 'O', ' ' and 'G'.")

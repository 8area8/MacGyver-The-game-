#! /usr/bin/env python3
# coding: utf-8

"""Core Game module."""

from core.modules.map_file import import_map
from core.modules.interface import Interface
from core.modules.musics import Music


class Game(Interface):
    """Core interface."""

    def __init__(self, images):
        """Init the game."""
        super().__init__()

        map_file = import_map()  # load the map.

        self.windows["menu"] = images["menu"]["menu"]

        self.musics = Music("game")
        self.musics.play_music()

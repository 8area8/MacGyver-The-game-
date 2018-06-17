#! /usr/bin/env python3
# coding: utf-8

"""Core Game module."""

from core.modules.map_file import import_map
from core.modules.interface import Interface
from core.modules.musics import Music
from core.game.map import Map


class Game(Interface):
    """Core interface."""

    def __init__(self, images):
        """Init the game."""
        super().__init__()

        self.map_ = Map(images, import_map())

        self.windows["menu"] = images["menu"]["menu"]

        self.musics = Music("game")
        self.musics.play_music()

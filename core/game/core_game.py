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

        map_ = Map(images, import_map())

        self.windows["menu"] = images["menu"]["menu"]
        self.windows["map"] = map_[0]
        self.windows["items"] = map_[1]
        self.windows["chara"] = map_[2]

        self.musics = Music("game")
        self.musics.play_music()

        self.player = None

        self.victory = False

    @property
    def in_action(self):
        """Test if the player is in an action."""
        return True if self.player.in_moove else False

    @property
    def remaining_items(self):
        """Count the last items to get."""
        return len(self.windows["items"])

    def start_events(self, events):
        """Game events."""
        pass

    def update(self):
        """Update the game."""
        pass

    def draw(self):
        """Draw the sprites."""
        area = self.windows
        main_area = area["main"]

        main_area.blit(area["menu"], (0, 0))
        area["map"].draw(main_area)
        area["items"].draw(main_area)
        area["chara"].draw(main_area)

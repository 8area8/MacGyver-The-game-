#! /usr/bin/env python3
# coding: utf-8

"""Core Game module."""

from pygame import key as pykey
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

from core.modules.map_file import import_map
from core.modules.interface import Interface
from core.modules.musics import Music
from core.game.map import Map
from core.modules.constants import MENU_Y, DIRECTION


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
        """Game events.

        In fact I don't need any event variable.
        """
        map_ = self.windows["map"]
        chara = self.windows["chara"]
        x, y = self.player.r_coords

        if self.in_action:
            return

        keys_pressed = pykey.get_pressed()
        for key in (K_DOWN, K_LEFT, K_RIGHT, K_UP):

            if not keys_pressed[key]:
                return
            dx, dy = DIRECTION[key.name]
            x, y = (x + dx, y + dy)
            if not map_[x, y] or map_[x, y].solid:
                return
            if chara[x, y]:
                self.change_to = "Generic"
                return

            self.player.start_moove(x, y)
            return

    def update(self):
        """Update the game."""
        if self.player.in_moove:
            self.player.moove()

        if self.player.coords in self.windows["items"].keys():
            name = self.windows["items"][self.player.coords].name
            self.player.items.apprend(name)
            self.windows["items"].suppr(self.player.coords)
            self.musics.play_sound("collect_point.ogg")

    def draw(self):
        """Draw the sprites."""
        area = self.windows
        main_area = area["main"]

        main_area.blit(area["menu"], (0, MENU_Y))
        area["map"].draw(main_area)
        area["items"].draw(main_area)
        area["chara"].draw(main_area)

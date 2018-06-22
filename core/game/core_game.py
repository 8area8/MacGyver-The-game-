#! /usr/bin/env python3
# coding: utf-8

"""Core Game module."""

from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, KEYDOWN

from core.modules.constants import MENU_Y, DIRECTION, ITEMS_POS, UPSCALE
from core.modules.map_file import import_map
from core.modules.interface import Interface
from core.game.sprite_text import TextItems
from core.modules.musics import Music
from core.game.player import Player
from core.game.map import Map


class Game(Interface):
    """Core interface."""

    def __init__(self, images):
        """Init the game."""
        super().__init__()

        map_ = Map(images, import_map())
        self.images = images

        self.windows["menu"] = images["menu"]["menu"]
        self.windows["map"] = map_[0]
        self.windows["items"] = map_[1]
        self.windows["chara"] = map_[2]

        self.musics = Music("game")
        self.musics.play_music()

        player_spawn = map_.player_spawn
        self.player = Player(images["characters"]["mcgayver"], player_spawn)

        self.text = TextItems()
        self.victory = False

    @property
    def in_action(self):
        """Test if the player is in an action."""
        return True if self.player.in_moove else False

    def start_events(self, event):
        """Game events.

        In fact I don't need events variable.
        """
        self._get_moove_keys(event)

    def _get_moove_keys(self, event):
        """Get a moove key to moove the player."""
        map_ = self.windows["map"]
        chara = self.windows["chara"]
        x, y = self.player.r_coords

        if self.in_action:
            return

        key = ""
        if event.type == KEYDOWN:
            if event.key == K_UP:
                key = "up"
            elif event.key == K_DOWN:
                key = "down"
            elif event.key == K_LEFT:
                key = "left"
            elif event.key == K_RIGHT:
                key = "right"
        if key:
            dx, dy = DIRECTION[key]
            x, y = (x + dx, y + dy)
            if not map_[x, y] or map_[x, y].solid:
                return
            if chara[x, y]:
                self.change_to = "Generic"
                final = "win" if len(self.player.items) >= 3 else "loose"
                self.images["final"] = self.images["backgrounds"][final]
                self.musics.stop_music()
                return

            self.player.start_moove(x, y, key)
            return

    def update(self):
        """Update the game."""
        if self.player.in_moove:
            self.player.moove()

        if self.player.r_coords in self.windows["items"].keys():
            item = self.windows["items"][self.player.r_coords]
            item.rect.x, item.rect.y = next(ITEMS_POS)
            self.player.items.add(item)
            self.windows["items"].suppr(self.player.r_coords)
            if len(self.player.items) > 2 and not self.victory:
                self.musics.play_sound("all_items.ogg")
                self.windows["menu"] = self.images["menu"]["menu_win"]
                self.victory = True
            else:
                self.musics.play_sound("collect_point.ogg")
        
        self.text.update(len(self.windows["items"]))

    def draw(self):
        """Draw the sprites."""
        area = self.windows
        main_area = area["main"]

        main_area.blit(area["menu"], (0, MENU_Y))
        main_area.blit(self.text.image, (self.text.coords))
        self.player.items.draw(main_area)
        area["map"].draw(main_area)
        area["items"].draw(main_area)
        area["chara"].draw(main_area)
        main_area.blit(self.player.image, self.player.t_coords)

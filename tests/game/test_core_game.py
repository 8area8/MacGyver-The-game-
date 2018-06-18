#! /usr/bin/env python3
# coding: utf-8

"""Test core_game module."""

import time

from pygame import display, mixer

from core.modules.constants import SCREEN_SIZE
from core.game.core_game import Game
from core.modules.images import collect_images


def test_core_game():
    """Test Game."""
    display.init()
    mixer.init()
    screen = display.set_mode(SCREEN_SIZE)

    images = collect_images()
    game = Game(images)

    game.start_events(None)
    game.update()
    game.draw()

    screen.blit(game.windows["main"], (0, 0))
    display.flip()

    time.sleep(3)

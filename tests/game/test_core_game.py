#! /usr/bin/env python3
# coding: utf-8

"""Test core_game module."""

import time

import pygame
from pygame import display, mixer, font

from core.modules.constants import SCREEN_SIZE
from core.game.core_game import Game
from core.modules.images import collect_images


def test_core_game():
    """Test Game."""
    font.init()
    display.init()
    mixer.init()
    screen = display.set_mode(SCREEN_SIZE)

    images = collect_images()
    game = Game(images)

    for event in pygame.event.get():
        game.start_events(event)
    game.update()
    game.draw()

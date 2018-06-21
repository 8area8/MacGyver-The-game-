#! /usr/bin/env python3
# coding: utf-8

"""Test the core Generic module."""

import pygame
from pygame import display, mixer

from core.modules.constants import SCREEN_SIZE
from core.generic.core_generic import Generic
from core.modules.images import collect_images


def test_generic():
    """Test the generic class."""
    display.init()
    mixer.init()
    screen = display.set_mode(SCREEN_SIZE)

    images = collect_images()
    images["final"] = images["backgrounds"]["win"]
    generic = Generic(images)

    for event in pygame.event.get():
        generic.start_events(event)
    generic.update()
    generic.draw()

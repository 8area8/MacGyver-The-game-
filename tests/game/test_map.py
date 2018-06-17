#! /usr/bin/env python3
# coding: utf-8

"""Test the map module."""

from pygame import display

from core.modules.map_file import import_map
from core.modules.images import collect_images
from core.modules.constants import SCREEN_SIZE
from core.game.map import Map


def test_map():
    """Test the map module."""
    display.init()
    display.set_mode(SCREEN_SIZE)

    images = collect_images()
    map_file = import_map()

    map_ = Map(images, map_file)
    assert map_[0][1, 10]

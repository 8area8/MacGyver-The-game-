#! /usr/bin/env python3
# coding: utf-8

"""Testing introduction file."""

from pygame import display, mixer

from core.modules.constants import SCREEN_SIZE
from core.introduction.core_intro import Introduction
from core.modules.images import collect_images


def test_core_intro():
    """Test Introduction."""
    display.init()
    mixer.init()
    display.set_mode(SCREEN_SIZE)

    images = collect_images()
    intro = Introduction(images)

    intro.start_events(None)
    intro.update()
    intro.draw()

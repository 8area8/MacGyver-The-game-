#! /usr/bin/env python3
# coding: utf-8

"""Dynamic text module."""

from pathlib import Path

import pygame

from core.modules.constants import UPSCALE


class TextItems(pygame.sprite.Sprite):
    """Dynamic text sprite."""

    def __init__(self):
        """Call the parent class (Sprite) constructor."""
        super().__init__()

        font = Path().resolve() / "assets" / "fonts" / "aerx.ttf"
        self.font = pygame.font.Font(str(font), 30 * UPSCALE)
        self.image = self.font.render("0", 0, (255, 255, 255))

        self.coords = (410 * UPSCALE, 483 * UPSCALE)

    def update(self, number):
        """Update."""
        self.image = self.font.render(str(number), 0, (255, 255, 255))

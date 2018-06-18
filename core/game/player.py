#! /usr/bin/env python3
# coding: utf-8

"""Player module."""

from core.modules.constants import CASE_PIXELS, SPEED


class Player:
    """Player's class."""

    def __init__(self, image, r_coords):
        """Initialize the player."""
        self.items = []
        self.image = image
        self.r_coords = r_coords

        self.in_moove = False
        self.direction = None
        self.speed = SPEED

    @property
    def t_coords(self):
        """Return the true coordinates."""
        x, y = self.r_coords
        return x * CASE_PIXELS, y * CASE_PIXELS

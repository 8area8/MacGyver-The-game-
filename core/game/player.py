#! /usr/bin/env python3
# coding: utf-8

"""Player module."""

from pygame.sprite import Group

from core.modules.constants import CASE_PIXELS, SPEED, DIRECTION, UPSCALE


class Player:
    """Player's class."""

    def __init__(self, image, t_coords):
        """Initialize the player."""
        self.items = Items()
        self.image = image
        self.t_coords = t_coords

        self.in_moove = False
        self.pace = None
        self.destination = None

    @property
    def r_coords(self):
        """Return the true coordinates."""
        x, y = self.t_coords
        return x // CASE_PIXELS // UPSCALE, y // CASE_PIXELS // UPSCALE

    def start_moove(self, x, y, direction):
        """Start a new player moove."""
        self.in_moove = True
        self.destination = x * CASE_PIXELS * UPSCALE, y * CASE_PIXELS * UPSCALE
        dx, dy = DIRECTION[direction]
        self.pace = dx * SPEED, dy * SPEED

    def moove(self):
        """Moove the player."""
        x, y = self.t_coords
        px, py = self.pace
        self.t_coords = x + px, y + py

        if self.t_coords == self.destination:
            self.in_moove = False


class Items(Group):
    """Little class for the items sprites."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
    
    def add(self, sprite=None):
        """Add a new item.
        
        Remove another.
        """
        if not sprite:
            return
        if len(self) == 3:
            removing = [i for i in self if i.coords == sprite.coords][0]
            self.remove(removing)
        super().add(sprite)

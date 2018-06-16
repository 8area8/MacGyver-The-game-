#! /usr/bin/env python3
# coding: utf-8

"""Map module."""


from pygame import sprite, image as pymage


class Map():
    """Initialize the game map."""

    def __init__(self, images):
        """Init the map."""
        self.layers = []

    def create_map(self, images):
        """Create the map."""
        for position in range(3):
            self.layer.append(Layer(position, images))

    def create_random_spawns(self):
        """Create random spawn for the items."""
        pass

    def __get_item__(self, key):
        """Get an item."""
        pass


class Layer(sprite.Group):
    """Contain a group of images."""

    def __init__(self, position, images):
        """Init the layer."""
        names = ("blocks", "characters", "objects")
        self.images = images[names[position]]

        self.coords = {}

    def __get_item__(self, key):
        """Get an item."""
        pass

    def __set_item__(self, key, value):
        """Set an item."""
        pass

    def keys(self):
        """Return the keys."""
        pass


class MapEntity(sprite.Sprite):
    """Represent an object in the labirynth."""

    def __init__(self, name, solid, image, coords):
        """Init the sprite."""
        self.name = name
        self.coords = coords
        self.solid = solid

        self.image = image
        self.rect = pymage.Rect()
        self.rect.x, self.rect.y = pymage.get_pos()

#! /usr/bin/env python3
# coding: utf-8

"""Map module."""

import random

from pygame import sprite


class Map():
    """The game map.

    This class works like a list of three layers.
    Use it by first specifying the index of the layer,
    and then the desired coordinates in the same layer.

    example: my_map[0][1, 2]  # coords 1, 2 of layer 0.
    """

    def __init__(self, images, map_file):
        """Initialize the map."""
        self._layers = list(Layer() for x in range(3))

        self.create_map(images, map_file)

    def create_map(self, images, map_file):
        """Create the map.

        Map[0] contains the structure (paths and walls).
        Map[1] contains the items.
        Map[2] contains the secondary characters (the guardian).
        """
        y = 0
        for line in map_file:
            x = 0
            for char in line:
                name = "wall" if char == "o" else "path"
                image = images["blocks"][name]
                self[0][x, y] = MapEntity(name, image, (x, y))

                self._create_characters(images["characters"]["guardian"], x, y)
                x += 1
            y += 1

        self._create_items(images["objects"])

    def _create_characters(self, image, x, y):
        """Create the secondary characters.

        NOTE: your can have more than one guardian.
        """
        if x == "G":
            self[2][x, y] = image

    def _create_items(self, images, items=("aiguille", "ether", "tube")):
        """Create the items.

        They appear randomly on the map.
        """
        coords = [key for key, v in self[0].items() if v.name == "path"]

        random_coords = (random.choice(coords) for x in range(len(items)))
        for coords, item in zip(random_coords, items):
            self[1][coords] = MapEntity(item, images[item], coords)

    def __getitem__(self, index):
        """Allow you to simply retrieve a value from self._layers.

        We will use "Map[index]".
        """
        try:
            self._layers[index]
        except IndexError as error:
            raise error
        else:
            return self._layers[index]


class Layer(sprite.Group):
    """Contain a group of images."""

    def __init__(self):
        """Init the layer."""
        super().__init__()

        self._coords = {}

    def __getitem__(self, key):
        """Allow you to simply retrieve a value from the group.

        We will use "Layer[key]".
        """
        try:
            self._coords[key]
        except KeyError as error:
            raise error
        else:
            return self._coords[key]

    def __setitem__(self, key, value):
        """Allow you to add values ​​to the group.

        We'll use "Layer[key] = value"

        The key must be a tuple that's correspond to coordinates,
        and the value an instance of MapEntity.
        """
        if key in self.keys():
            self.remove(self._coords[key])

        self.add(value)
        self._coords[key] = value

    def __len__(self):
        """Return the dict len."""
        return len(self._coords)

    def keys(self):
        """Return the keys."""
        return self._coords.keys()

    def items(self):
        """Return the items."""
        return self._coords.items()


class MapEntity(sprite.Sprite):
    """Represent an object in the labirynth."""

    def __init__(self, name, image, coords):
        """Init the sprite."""
        super().__init__()

        self.name = name
        self.coords = coords
        self.solid = True if name == "wall" else False

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.coords

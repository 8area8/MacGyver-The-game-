#! /usr/bin/env python3
# coding: utf-8

"""Map module."""


from pygame import sprite, image as pymage


class Map():
    """The game map.

    This class works like a list of three layers.
    Use it by first specifying the index of the layer,
    and then the desired coordinates in the same layer.

    example: my_map[0][1, 2]  # coords 1, 2 of layer 0.
    """

    def __init__(self, images, map_file):
        """Init the map."""
        self._layers = []

    def create_map(self, images):
        """Create the map."""
        for position in range(3):
            self._layers.append(Layer(position, images))

    def create_random_spawns(self):
        """Create random spawn for the items."""
        pass

    def __get_item__(self, index):
        """Allow you to simply retrieve a value from the group.

        We will use "Map[index]".
        """
        try:
            self._layers[index]
        except IndexError:
            raise IndexError()
        else:
            return self._coords[index]


class Layer(sprite.Group):
    """Contain a group of images."""

    def __init__(self, position, images):
        """Init the layer."""
        names = ("blocks", "characters", "objects")
        self.images = images[names[position]]

        self._coords = {}

    def __getitem__(self, key):
        """Allow you to simply retrieve a value from the group.

        We will use "Layer[key]".
        """
        if key in self.keys():
            return self._coords[key]
        raise KeyError(f"The key '{key}' doesn't exist!")

    def __setitem__(self, key, value):
        """Allow you to add values ​​to the group.

        We'll use "Layer[key] = value"

        The key must be a tuple that's correspond to coordinates,
        and the value an instance of LabyrinthSprite.
        """
        if key in self.keys():
            self.remove(self.coords[key])

        self.add(value)
        self._coords[key] = value

    def keys(self):
        """Return the keys."""
        return self.coords.keys()


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

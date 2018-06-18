#! /usr/bin/env python3
# coding: utf-8

"""Map module."""

from random import shuffle

from pygame import sprite

from core.modules.constants import CASE_PIXELS as pixels, ITEMS


class Map():
    """The game map.

    This class works like a list of three layers.
    Use it by first specifying the index of the layer,
    and then the desired coordinates in the same layer.

    example: my_map[0][1, 2]  # coords 1, 2 of layer 0.

    NOTE: Map contains 3 layers. Read the "create_map" documentation
    for more details.
    """

    def __init__(self, images, map_file):
        """Initialize the map."""
        self._layers = [Layer() for x in range(3)]
        self.player_spawn = None
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
                self._create_structure(images, char, (x, y))
                self._create_characters(images, char, (x, y))
                x += 1
            y += 1

        self._create_items(images["objects"])
        self._create_player_spawn()

    def _create_structure(self, images, char, coords):
        """Create the core structure (paths and walls)."""
        name = "wall" if char == "O" else "path"
        image = images["blocks"][name]
        self[0][coords] = MapEntity(name, image, coords)

    def _create_characters(self, images, char, coords):
        """Create the secondary characters.

        NOTE: your can have more than one guardian.
        """
        if char == "G":
            image = images["characters"]["guardian"]
            self[2][coords] = MapEntity("guardian", image, coords)

    def _create_items(self, images):
        """Create the items.

        They appear randomly on the map.
        """
        coords = (c for c, v in self[0].items() if v.name == "path")
        coords = [c for c in coords if not self[2][c]]  # avoid guardian cases
        shuffle(coords)

        for i in range(len(ITEMS)):
            pos, name = coords[i], ITEMS[i]
            self[1][pos] = MapEntity(name, images[name], pos)

    def _create_player_spawn(self):
        """Create a random spawn for the player."""
        coords = (c for c, v in self[0].items() if v.name == "path")
        coords = (c for c in coords if not self[2][c])
        coords = [c for c in coords if not self[1][c]]
        shuffle(coords)
        x, y = coords.pop()
        self.player_spawn = x * pixels, y * pixels

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
    """A group of Sprites, with some dict methods."""

    def __init__(self):
        """Initialize the layer."""
        super().__init__()
        self._coords = {}

    def __getitem__(self, key):
        """Allow you to simply retrieve a value from the dict.

        We will use "Layer[key]".
        """
        try:
            self._coords[key]
        except KeyError:
            return None
        else:
            return self._coords[key]

    def __setitem__(self, key, value):
        """Allow you to add values ​​to the dict.

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
        """Return the dict keys."""
        return self._coords.keys()

    def items(self):
        """Return the dict items."""
        return self._coords.items()

    def suppr(self, key):
        """Remove an sprite by a key."""
        if not self[key]:
            return None
        self.remove(self._coords[key])
        del self._coords[key]


class MapEntity(sprite.Sprite):
    """Sprite that represents an object in the labyrinth."""

    def __init__(self, name, image, coords):
        """Initialize the sprite."""
        super().__init__()

        self.name = name
        x, y = coords
        self.coords = (x * pixels, y * pixels)
        self.solid = True if name == "wall" else False

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.coords

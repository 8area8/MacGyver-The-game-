#! /usr/bin/env python3
# coding: utf-8

"""Introduction file."""

from core.modules.interface import Interface


class Introduction(Interface):
    """The first called interface.

    Display an image and play a music for three seconds.
    """

    def __init__(self, images):
        """Initialize the core variables."""
        super().__init__()

        self.name = "introduction"
        self.windows = {}
        self.musics = None

        self.timer = 0
        self.max_timer = 90

        # jouer la musique
        # afficher l'image.

    def start_events(self, events):
        """No events."""
        pass

    def update(self):
        """Update the timer."""
        self.timer += 1
        if self.timer == self.max_timer:
            self.name = "game"

    def draw(self):
        """Draw the elements."""
        pass

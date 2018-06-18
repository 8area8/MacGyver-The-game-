#! /usr/bin/env python3
# coding: utf-8

"""Introduction file."""

from core.modules.interface import Interface
from core.modules.musics import Music


class Introduction(Interface):
    """The first called interface.

    Display an image and play a music for three seconds.
    """

    def __init__(self, images):
        """Initialize the core variables."""
        super().__init__()

        self.windows["bg"] = images["backgrounds"]["intro"]

        self.musics = Music("introduction")
        self.musics.play_music()

        self.timer = 0
        self.max_timer = 90

    def start_events(self, events):
        """No events."""
        pass

    def update(self):
        """Update the timer."""
        self.timer += 1
        if self.timer == self.max_timer:
            self.musics.stop_music()
            self.change_to = "Game"

    def draw(self):
        """Draw the elements."""
        self.windows["main"].blit(self.windows["bg"], (0, 0))

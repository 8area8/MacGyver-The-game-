#! /usr/bin/env python3
# coding: utf-8

"""Contain the abstract class Interface.

Used for others interfaces.
"""


class Interface:
    """Define all the interface of the game."""

    def __init__(self):
        """Initialize the core variables."""
        self.name = ""
        self.windows = {}
        self.musics = None

    def start_events(self, events):
        """Use pygame event to do things."""
        raise NotImplementedError()

    def update(self):
        """Update the interface variables."""
        raise NotImplementedError()

    def draw(self):
        """Draw the surfaces."""
        raise NotImplementedError()

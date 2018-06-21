#! /usr/bin/env python3
# coding: utf-8

"""Core Generic module."""


import pygame
from pygame import display, mixer

from core.modules.interface import Interface
from core.modules.musics import Music


class Generic(Interface):
    """Display the victory screen."""
    
    def __init__(self, images):
        """Initialize Generic."""
        super().__init__()

        self.windows["background"] = images["backgrounds"]["generic"]
        self.windows["final"] = images["final"]

        self.musics = Music("generic")
        self.musics.play_sound("jingle_win.ogg")
    
    def start_events(self, event):
        """Events."""
        if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONUP):
            self.running = False
    
    def update(self):
        """Update the Generic."""
        pass
    
    def draw(self):
        """Draw the elements."""
        self.windows["main"].blit(self.windows["background"], (0, 0))
        self.windows["main"].blit(self.windows["final"], (0, 0))

#! /usr/bin/env python3
# coding: utf-8

"""Core Music class."""

import os
from pathlib import Path

from pygame import mixer


class Music:
    """Call it to play sounds and musics.

    "folder_name" values are "introduction", "game" and "generic".

    The Music module can contain x sounds but only one music.
    NOTE: musics files must be in .wav or .ogg !
    """

    def __init__(self, folder_name):
        """Init sounds and musics."""
        path = Path().resolve() / "assets" / "musics_sounds" / folder_name
        self.sounds = {}

        for music in os.listdir(str(path / "musics")):
            mixer.music.load(str(path / "musics" / music))

        for sound in os.listdir(str(path / "sounds")):
            self.sounds[sound] = mixer.Sound(str(path / "sounds" / sound))

    def play_music(self):
        """Play a music."""
        mixer.music.play(loops=-1)

    def play_sound(self, name):
        """Play a sound."""
        self.sounds[name].play()

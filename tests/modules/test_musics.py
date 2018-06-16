#! /usr/bin/env python3
# coding: utf-8

"""Test Music class."""


from pathlib import Path
from os import listdir

from pygame import mixer

from core.modules.musics import Music


def test_music():
    """Test tall sound/music in the musics module."""
    mixer.pre_init(44100, -16, 2, 2048)
    mixer.init(44100, -16, 2, 2048)

    path = Path().resolve() / "assets" / "musics_sounds"

    for folder in listdir(str(path)):
        musics = Music(folder)
        musics.play_music()

        for sound in listdir(str(path / folder / "sounds")):
            musics.play_sound(sound)

    musics.stop_music()

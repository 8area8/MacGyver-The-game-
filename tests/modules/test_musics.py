#! /usr/bin/env python3
# coding: utf-8

"""Test Music class."""


from pygame import mixer

from core.modules.musics import Music


def test_music():
    """Test the music module."""
    mixer.pre_init(44100, -16, 2, 2048)
    mixer.init(44100, -16, 2, 2048)

    musics = Music("game")
    musics.play_music()
    musics.play_sound("collect_point.wav")

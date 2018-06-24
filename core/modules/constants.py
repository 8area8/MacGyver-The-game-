#! /usr/bin/env python3
# coding: utf-8

"""Contain all constants variables.

Works with a config file.
NOTE: if the config file doesn't exist, we create it with some default values.
"""

import configparser
from os import path, listdir
from pathlib import Path


CONF = configparser.ConfigParser()
if not path.exists('config.ini'):
    CONF['size'] = {'case_pixels': '32', 'upscale': '1'}
    CONF['moove'] = {'speed': '8'}
    CONF.write(open('config.ini', 'w'))
else:
    CONF.read("config.ini")

# SIZES
UPSCALE = int(CONF["size"]["upscale"])
CASE_PIXELS = int(CONF["size"]["case_pixels"])
SCREEN_SIZE = (CASE_PIXELS * 15 * UPSCALE, CASE_PIXELS * 16 * UPSCALE)

# MOVEMENT
DIRECTION = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
SPEED = int(CONF["moove"]["speed"]) if int(CONF["moove"]["speed"]) in (4, 8) else 8 * UPSCALE

# ITEMS NAME
ITEMS = [i[:-4] for i in listdir(Path() / "assets" / "images" / "objects")]

# IMAGES COORDINATES
MENU_Y = CASE_PIXELS * 15 * UPSCALE


def _items_pos():
    """Return a position for an item."""
    i = 0
    pos = ((0, MENU_Y), (51 * UPSCALE, MENU_Y), (102 * UPSCALE, MENU_Y))
    while True:
        yield pos[i][0], pos[i][1]
        i = (i + 1) % 3
ITEMS_POS = _items_pos()

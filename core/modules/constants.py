#! /usr/bin/env python3
# coding: utf-8

"""Contain all constants variables.

Works with a config file.
NOTE: if the config file doesn't exist, we create it with some default values.
"""

import configparser
from os import path, listdir
from pathlib import Path


conf = configparser.ConfigParser()
if not path.exists('config.ini'):
    conf['size'] = {'case_pixels': '32', 'upscale': '1'}
    conf['moove'] = {'speed': '4'}
    conf.write(open('config.ini', 'w'))
else:
    conf.read("config.ini")

# SIZES
CASE_PIXELS = int(conf["size"]["case_pixels"])
UPSCALE = int(conf["size"]["upscale"])
SCREEN_SIZE = (CASE_PIXELS * 15 * UPSCALE, CASE_PIXELS * 16 * UPSCALE)

# MOVEMENT
DIRECTION = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
SPEED = int(conf["moove"]["speed"])

# ITEMS NAME
items_path = Path().resolve() / "assets" / "images" / "objects"
ITEMS = [i[:-4] for i in listdir(str(items_path))]

# IMAGES COORDINATES
MENU_Y = CASE_PIXELS * 15 * UPSCALE
ITEMS_POS = {"aiguille": (0, MENU_Y), "ether": (51 * UPSCALE, MENU_Y),
             "tube": (102 * UPSCALE, MENU_Y)}

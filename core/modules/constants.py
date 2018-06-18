#! /usr/bin/env python3
# coding: utf-8

"""Contain all constants variables."""

import configparser


conf = configparser.ConfigParser()
conf.read("config.ini")

# SIZES
CASE_PIXELS = int(conf["size"]["case_pixels"])
UPSCALE = int(conf["size"]["upscale"])
SCREEN_SIZE = (CASE_PIXELS * 15 * UPSCALE, CASE_PIXELS * 16 * UPSCALE)

# MOVEMENT
DIRECTION = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
SPEED = int(conf["moove"]["speed"])

# IMAGES COORDINATES
MENU_Y = CASE_PIXELS * 15 * UPSCALE

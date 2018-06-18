#! /usr/bin/env python3
# coding: utf-8

"""Contain all constants variables."""

import configparser


conf = configparser.ConfigParser()
conf.read("config.ini")


CASE_PIXELS = int(conf["size"]["case_pixels"])
UPSCALE = int(conf["size"]["upscale"])

SCREEN_SIZE = (CASE_PIXELS * 15 * UPSCALE, CASE_PIXELS * 16 * UPSCALE)


# IMAGES COORDINATES

# Game

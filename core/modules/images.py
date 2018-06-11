#! /usr/bin/env python3
# coding: utf-8

"""Core images file.

NOTE:
be carefull with the "images" folder!
It must contain only folders, which themselves must contain only images.
There is no test to know if you use the "images" folder safely.
"""

import os
from pathlib import Path

import pygame

from core.modules import constants as cst


def collect_images():
    """Collect all images and put them in a dict."""
    path = Path().resolve() / "assets" / "images"
    images = {}

    for folder in os.listdir(str(path)):
        images[folder] = _fill_in(path / folder)

    return images


def _fill_in(path):
    """Fill in the folder of his images.

    Return a dict who contain all images as pygame Surface.
    """
    images = {}
    for image in os.listdir(str(path)):
        without_ext = image[:-4]
        images[without_ext] = _create_image(path / image)

    return images


def _create_image(path):
    """Create and return a pygame image from a path.

    if the upscale variable of the constant module is greater than 1,
    then we upscale the image.
    """
    image = pygame.image.load(str(path)).convert_alpha()

    if cst.UPSCALE > 1:
        image = _upscale(image)

    return image


def _upscale(image):
    """Upscale an return an image."""
    upscale = cst.UPSCALE
    w, h = image.get_size()

    upscaled_size = ((w * upscale), (h * upscale))
    upscaled_image = pygame.transform.scale(image, upscaled_size)

    return upscaled_image

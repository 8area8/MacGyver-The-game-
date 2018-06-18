"""Testing images file."""

import pygame

from core.modules.images import collect_images
from core.modules.constants import SCREEN_SIZE


def test_collect_images():
    """Test if all images are collected."""
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE)

    folder = collect_images()

    for images in folder.values():
        for image in images.values():
            assert isinstance(image, pygame.Surface)

    # The way we use it:
    assert isinstance(folder["backgrounds"]["generic"], pygame.Surface)

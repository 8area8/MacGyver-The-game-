"""Testing images file."""

import pygame

from core.modules.images import collect_images


def test_collect_images():
    """Test if all images are collected."""
    pygame.init()
    pygame.display.set_mode((1280, 720))

    folder = collect_images()

    for images in folder.values():
        for image in images.values():
            assert isinstance(image, pygame.Surface)

    # The way we use it:
    assert isinstance(folder["backgrounds"]["generic"], pygame.Surface)

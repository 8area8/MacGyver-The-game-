#! /usr/bin/env python3
# coding: utf-8

"""Launch the game from this file."""

import importlib

import pygame
from pygame.locals import QUIT

from core.modules.constants import SCREEN_SIZE
from core.modules.images import collect_images
from core.introduction.core_intro import Introduction


def main():
    """Launch the game."""
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()  # Initialize pygame.

    pygame.display.set_caption('MacGyver')  # We choose a title.
    main_screen = pygame.display.set_mode(SCREEN_SIZE)  # the main window.

    images = collect_images()  # load all images.
    interface = Introduction(images)
    fps = pygame.time.Clock()
    running = True

    while(running):

        interface = get_new_interface(interface)

        # Events section.
        for event in pygame.event.get():  # Events call.
            if event.type == QUIT:
                running = False
            interface.start_events(event)  # Ours variable events call.

        # Update section.
        interface.update()

        # Drawing section.
        interface.draw()
        main_screen.blit(interface.windows["main"], (0, 0))

        # Screen refreshness.
        pygame.display.flip()

        # Control the frames per second (want 30 fps).
        fps.tick(30)


def get_new_interface(interface):
    """Change to another interface if "change_to" got value."""
    if interface.change_to:
        name = interface.change_to
        path = f"core.{name.lower()}.core_{name.lower()}"
        return getattr(importlib.import_module(path), name)()
    return interface


if __name__ == "__main__":
    main()

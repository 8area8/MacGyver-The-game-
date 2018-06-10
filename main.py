#! /usr/bin/env python3
# coding: utf-8

"""Launch the game from this file."""


import pygame
from pygame.locals import QUIT

import core.modules.images as images


def main():
    """Launch the game."""
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()  # Initialize pygame.

    pygame.display.set_caption('MacGyver')  # We choose a title.
    main_screen = pygame.display.set_mode((1280, 720))  # the main window.

    # importation des images
    fps = pygame.time.Clock()
    interface = None
    running = True

    while(running):

        get_new_interface(interface)

        # Events section.
        for event in pygame.event.get():  # Events call.
            if event.type == QUIT:
                running = False
            interface.start_events(event)  # Ours variable events call.

        # Update section.
        interface.update()

        # Drawing section.
        interface.draw()
        main_screen.blit(interface.sprt.main_surface, (0, 0))

        # Screen refreshness.
        pygame.display.flip()

        # Control the frames per second (want 30 fps).
        fps.tick(30)


def get_new_interface(interface):
    """Change to another interface if his name got a new value."""
    pass


if __name__ == "__main__":
    main()

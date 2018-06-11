#! /usr/bin/env python3
# coding: utf-8

"""Launch the game from this file."""


import pygame
from pygame.locals import QUIT

from core.modules.images import collect_images


def main():
    """Launch the game."""
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()  # Initialize pygame.

    pygame.display.set_caption('MacGyver')  # We choose a title.
    main_screen = pygame.display.set_mode((960, 960))  # the main window.

    images = collect_images()  # load all images.
    interface = Introduction(images)
    fps = pygame.time.Clock()
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

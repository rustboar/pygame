import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # the actual game
    while pygame.init():
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # sets fps to 60
        dt = clock.tick(60) / 1000

    screen.fill("black")


if __name__ == "__main__":
    main()

import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    PLAYER_LIVES = 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shot)
    AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # the actual game
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # sets fps to 60
        dt = clock.tick(60) / 1000
        # updates game state
        updatable.update(dt)
        # collision check
        for aster in asteroids:
            if aster.collides_with(player):
                if PLAYER_LIVES == 0:
                    log_event("player_died")
                    print(f"Your score was {score}")
                    print("Game over!")
                    sys.exit()
                log_event("player_hit")
                PLAYER_LIVES -= 1
                player.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            for i in shot:
                if aster.collides_with(i):
                    log_event("asteroid_shot")
                    aster.split()
                    i.kill()
                    score += 1
        # renders game state
        screen.fill("black")
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()

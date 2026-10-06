import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Initializing  pygame
    pygame.init()

    # FPS
    clock = pygame.time.Clock()
    dt = 0.0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # AsteroidField
    asteroidfield = AsteroidField()

    # Creating the GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Player Object
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for obj in asteroids:
            for bullet in shots:
                if bullet.collides_with(obj):
                    log_event("asteroid_shot")
                    bullet.kill()
                    obj.split()
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)


if __name__ == "__main__":
    main()

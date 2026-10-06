import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

    # Class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

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
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)


if __name__ == "__main__":
    main()

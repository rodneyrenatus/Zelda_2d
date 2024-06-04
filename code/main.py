import pygame
import sys
from settings import *
from level import Level
import os


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH), pygame.FULLSCREEN)
        pygame.display.set_caption('MY LIFE IN 2D :)')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        main_sound = pygame.mixer.Sound(
            os.path.join("Lunar's Zelda Style Game", 'level graphics', 'audio', 'main.ogg'))
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

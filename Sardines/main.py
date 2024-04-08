import pygame
from sprites import *
from config import *
import sys
import time
import random
#asterisk means all

 # Window
WIDTH = 1350
HEIGHT = 400
pygame.display.set_caption("Sardines")

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def running(self):
        self.running = True

    def new(self):
        self.playing = True
        #How the sprites are layered e.g. ground below player
        self.blocks = pygame.sprite.LayeredUpdates()
        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1, 2) 

    def intro(self):
        pass

    def end(self):
        pass

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(RED)
        self.all_sprites.draw(self.screen)
        #How many times the screen updates so it wont freeze(in config)
        self.clock.tick(FPS)
        pygame.display.update()

    def events(self):
        #Closing and stopping all
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def main(self):
        #Initializing all methods
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

Game.new()
while Game.running:
    Game.main()

pygame.quit()
sys.exit()
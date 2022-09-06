import pygame
import random
from Settings import *


class Player:
    def __init__(self, window):
        # player icon and settings
        self.window = window
        self.poz_x = WIDTH / 2
        self.poz_y = HEIGHT / 2
        self.poz_in_map = (0, 0)
        self.player_img_1 = pygame.transform.scale(pygame.image.load("Img/player_1.png"), (100, 80))
        self.player_img_2 = pygame.transform.scale(pygame.image.load("Img/player_2.png"), (100, 80))
        self.player_img_3 = pygame.transform.scale(pygame.image.load("Img/player_3.png"), (100, 80))
        # back ground
        self.bg = pygame.transform.scale(pygame.image.load("Img\preview-3_orig.jpg"), (1100, 700))
        self.bg_x = 0

    def rend(self, command):
        self.poz_y += 5
        self.rend_bg()
        self.window.blit(command, (self.poz_x - 200, self.poz_y))

    def rend_bg(self):
        self.bg_x -= 2
        self.window.blit(self.bg, (self.bg_x, 0))
        if (self.bg_x >= -1100) and (self.bg_x <= -1100 + WIDTH):
            self.window.blit(self.bg, (self.bg_x + 1100, 0))
        if self.bg_x == -1100:
            self.bg_x = 0

    def moving(self):
        self.poz_y -= 10
        self.rend(self.player_img_3)


class Tube:
    def __init__(self, window, x, score):
        self.window = window
        self.x = x
        self.y = 150 + random.randint(150, 450)
        self.top_tube = pygame.transform.scale(pygame.image.load("Img/tube_top.jpg.png"), (98, 47))
        self.body_tube = pygame.transform.scale(pygame.image.load("Img/tube.jpg.png"), (90, 822))

        self.score_bar = score
        self.rect_1 = pygame.Rect(self.x, self.y, 90, 822)
        self.rect_2 = pygame.Rect(self.x, self.y - 120 - 822, 90, 822)

    def rend(self, player_poz):
        self.move(player_poz)
        # down
        self.window.blit(self.body_tube, (self.x, self.y))
        self.window.blit(self.top_tube, (self.x - 4, self.y))
        # upper
        self.window.blit(self.body_tube, (self.x, self.y - 120 - 822))
        self.window.blit(self.top_tube, (self.x - 4, self.y - 120 - 47))

    def move(self, player_poz):
        self.x -= 2
        if self.x == 100:
            self.score_bar[0] += 1
        if self.x == -120:
            self.x = 1380
            self.y = 150 + random.randint(150, 550)
        self.rect_1 = pygame.Rect(self.x+90, self.y, 90, 822)
        self.rect_2 = pygame.Rect(self.x+90, self.y - 120 - 822, 90, 822)
        if self.rect_1.collidepoint((player_poz[0]-10, player_poz[1] + 55)):
            exit()
        if self.rect_1.collidepoint((player_poz[0] - 80, player_poz[1] + 55)):
            exit()
        if self.rect_2.collidepoint((player_poz[0]-10, player_poz[1]+10)):
            exit()
        if self.rect_2.collidepoint((player_poz[0] - 80, player_poz[1]+10)):
            exit()

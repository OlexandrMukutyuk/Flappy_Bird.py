# import pygame
# from Settings import *
from Obj import *
pygame.init()

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.anim_time = 0
        self.clok = pygame.time.Clock()
        self.score_bar = [0]
        self.main_font = pygame.font.Font(None, 40)
        self.player = Player(self.window)

        self.tube = [Tube(self.window, 300, self.score_bar), Tube(self.window, 600, self.score_bar),
                     Tube(self.window, 900, self.score_bar), Tube(self.window, 1200, self.score_bar),
                     Tube(self.window, 1500, self.score_bar)]

        self.run()

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.player.moving()
                self.anim_time = 0
            elif self.anim_time == 13:
                self.player.rend(self.player.player_img_2)
            else:
                self.player.rend(self.player.player_img_1)
                self.anim_time += 1
            self.tube_rend()

            pygame.display.update()
            self.clok.tick(60)

    def tube_rend(self):
        for item in self.tube:
            item.rend((self.player.poz_x,self.player.poz_y))
            self.window.blit(self.main_font.render(str(self.score_bar[0]), True, (255, 255, 255)), (50, 50))


if __name__ == '__main__':
    Game()

import pygame
from blocks import gtpx,gtpy

class board:
    def __init__(self,dimx,dimy,ecran):
        self.name = f'{dimx}x{dimy}'
        self.dimx = dimx
        self.dimy = dimy
        self.screen = ecran
        self.config = [['W']+['E' for i in range(dimx)]+['W'] for j in range(dimy)] + \
                      [['W' for i in range(dimx+2)]]
        wall_block = pygame.image.load(r'textures/grey.png').convert()
        wall_block = pygame.transform.scale(wall_block, (20, 20))
        bg_block = pygame.image.load(r'textures/black.png').convert()
        bg_block = pygame.transform.scale(bg_block, (20, 20))
        blue_block = pygame.image.load(r'textures/blue.png').convert()
        blue_block = pygame.transform.scale(blue_block, (20, 20))
        purple_block = pygame.image.load(r'textures/purple.png').convert()
        purple_block = pygame.transform.scale(purple_block, (20, 20))
        yellow_block = pygame.image.load(r'textures/yellow.png').convert()
        yellow_block = pygame.transform.scale(yellow_block, (20, 20))
        cyan_block = pygame.image.load(r'textures/cyan.png').convert()
        cyan_block = pygame.transform.scale(cyan_block, (20, 20))
        orange_block = pygame.image.load(r'textures/orange.png').convert()
        orange_block = pygame.transform.scale(orange_block, (20, 20))
        green_block = pygame.image.load(r'textures/green.png').convert()
        green_block = pygame.transform.scale(green_block, (20, 20))
        red_block = pygame.image.load(r'textures/red.png').convert()
        red_block = pygame.transform.scale(red_block, (20, 20))
        self.textures = {'E': bg_block, 'W': wall_block, 'B': blue_block, 'P': purple_block,
                         'Y': yellow_block, 'C': cyan_block, 'O':orange_block, 'G': green_block,
                         'R': red_block}
    def __repr__(self):
        return f'Plateau {self.name}'

    def plot(self):
        for y in range(len(self.config)):
            for x in range(len(self.config[y])):
                self.screen.blit(self.textures[self.config[y][x][-1]],(160+x*20,80+y*20))
        pygame.display.flip()




if __name__=='__main__':
    b = board(12,22,5)
    for l in b.config:
        print(l)



import pygame.event
from board import *
from blocks import *
from scoreboard import *
from random import randrange
from time import time

def timer(t):
    if t<15: y=1
    elif t<105: y=1-0.005*t
    else: y = 0.475
    return y

if __name__ == '__main__':
    # Initialisation
    tetriminos = {'I': Tetri_I, 'T': Tetri_T, 'L': Tetri_L, 'J': Tetri_J, 'O': Tetri_O, 'S': Tetri_S, 'Z': Tetri_Z}
    tet_keys = [k for k in tetriminos.keys()]

    # Jeu
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/main_theme.wav')

    screen = pygame.display.set_mode((1000,600))
    game_over = pygame.image.load(r'textures/game_over.png').convert()
    pygame.mixer.music.play(-1)


    plateau = board(12,22,screen)
    plateau.plot()
    SBoard = ScoreBoard(screen)
    SBoard.plot()
    preview = tetriminos[tet_keys[randrange(7)]]('pre', 280,20,screen,plateau,SBoard)
    preview.add(plot=True,inside=False)
    currenT = tetriminos[tet_keys[randrange(7)]]('cur',280,80,screen,plateau,SBoard)
    status = currenT.add(plot=True)
    clock = time()
    depart = time()
    while True:
        while status:
            #Gestion des évenements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    record_file = open('record.txt','w')
                    record_file.write(str(SBoard.record))
                    record_file.close()
                    pygame.quit()


            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                record_file = open('record.txt','w')
                record_file.write(str(SBoard.record))
                record_file.close()
                pygame.quit()

            #Code du jeu
            if keys[pygame.K_UP]:
                currenT.rotate()
                #plateau.plot()

            if keys[pygame.K_RIGHT]:
                currenT.move_R()
                #plateau.plot()

            if keys[pygame.K_LEFT]:
                currenT.move_L()
                #plateau.plot()

            if keys[pygame.K_DOWN]:
                currenT.move_D()
                #plateau.plot()

            if currenT.end_fall():
                preview.erase(plot=True,skem=False)
                currenT = tetriminos[preview.type]('cur',280,80,screen,plateau,SBoard)
                preview = tetriminos[tet_keys[randrange(7)]]('pre', 280,20,screen,plateau,SBoard)
                preview.add(plot=True,inside=False)
                status = currenT.add(plot=False)
                if status:
                    plateau.plot()
                else:
                    screen.blit(game_over,(200,250))
                    pygame.display.flip()

            if time()-clock>timer(time()-depart):
                clock = time()
                currenT.move_D()
                #plateau.plot()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                record_file = open('record.txt','w')
                record_file.write(str(SBoard.record))
                record_file.close()
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            record_file = open('record.txt','w')
            record_file.write(str(SBoard.record))
            record_file.close()
            pygame.quit()
        if keys[pygame.K_RETURN]:
            plateau = board(12,22,screen)
            plateau.plot()
            SBoard.score = 0
            SBoard.plot()
            preview.erase(plot=True,skem=False)
            currenT = tetriminos[tet_keys[randrange(7)]]('cur',280,80,screen,plateau,SBoard)
            preview = tetriminos[tet_keys[randrange(7)]]('pre', 280,20,screen,plateau,SBoard)
            preview.add(plot=True,inside=False)
            status = currenT.add(plot=True)

            plateau.plot()
            clock = time()
            depart = time()


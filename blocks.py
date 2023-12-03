import pygame
from time import sleep

class Tetriminos:
    def __init__(self, name, posx, posy, ecran, plat, scoreboard):
        self.name = name
        self.posx = posx
        self.gridx =(self.posx-160)//20
        self.posy = posy
        self.gridy = (self.posy-80)//20
        self.screen = ecran
        self.position = 0
        self.geometry = []
        self.orientations = []
        self.color = 0
        self.type = ''
        self.back = pygame.image.load(r'textures/black.png').convert()
        self.back = pygame.transform.scale(self.back, (20, 20))
        self.board = plat
        self.textures = plat.textures
        self.scoreboard = scoreboard

    def __repr__(self):
        for ligne in self.geometry:
            for bloc in ligne:
                if bloc == 1:
                    print("O", end='')
                else:
                    print(" ", end='')
            print("")

    def grid_to_pos(self):
        self.posx = self.gridx*20+160
        self.posy = self.gridy*20+80

    def pos_to_grid(self):
        self.gridx =(self.posx-160)//20
        self.gridy = (self.posy-80)//20


    def add(self,plot=False,inside=True):
        status = True
        for i in range(len(self.geometry)):
            for j in range(len(self.geometry[i])):
                if self.geometry[i][j] == 1:
                    if inside:
                        if self.board.config[self.gridy+i][self.gridx+j]!='E':
                            return False
                        else:
                            self.board.config[self.gridy+i][self.gridx+j] = 'B'+self.color
                            if plot:
                                self.screen.blit(self.textures[self.color],(gtpx(self.gridx+j),gtpy(self.gridy+i)))
                    else:
                        self.screen.blit(self.textures[self.color],(gtpx(self.gridx+j),gtpy(self.gridy+i)))
        pygame.display.flip()
        return(status)

    def erase(self,plot,skem=True):
        for i in range(len(self.geometry)):
            for j in range(len(self.geometry[i])):
                if self.geometry[i][j] == 1:
                    if skem:
                        self.board.config[self.gridy+i][self.gridx+j] = 'E'
                    if plot:
                        self.screen.blit(self.textures['E'],(gtpx(self.gridx+j),gtpy(self.gridy+i)))
                else:
                    pass

    def erase_line(self,i):
        for j in range(1,self.board.dimx+1):
            self.board.config[i][j] = 'E'

    def is_ok(self,modx,mody):
        x_est = ((self.posx + modx)-160)//20
        y_est = ((self.posy + mody)-100)//20
        ok = True
        for i in range(len(self.geometry)):
            for j in range(len(self.geometry[i])):
                if self.geometry[i][j] == 1:
                    if self.board.config[y_est+i+1][x_est+j][0] == 'W':
                        ok = False
                else:
                    pass
        return ok

    def is_ok_rotate(self):
        x_est = (self.posx-160)//20
        y_est = (self.posy-100)//20
        geo_est = self.orientations[(self.position+1)%4]
        ok = True
        for i in range(len(geo_est)):
            for j in range(len(geo_est[i])):
                if geo_est[i][j] == 1:
                    if self.board.config[y_est+i+1][x_est+j][0] == 'W':
                        ok = False
                else:
                    pass
        return ok

    def rotate(self):
        if self.is_ok_rotate():
            self.erase(plot=True)
            self.position = (self.position+1)%4
            self.geometry = self.orientations[self.position]
            self.add(plot=True)
            sleep(0.14)

    def move_R(self):
        if self.is_ok(20,0):
            self.erase(plot=True)
            self.posx = self.posx +20
            self.pos_to_grid()
            self.add(plot=True)
            sleep(0.09)


    def move_L(self):
        if self.is_ok(-20,0):
            self.erase(plot=True)
            self.posx = self.posx -20
            self.pos_to_grid()
            self.add(plot=True)
            sleep(0.09)

    def move_D(self):
        if self.is_ok(0,20):
            self.erase(plot=True)
            self.posy = self.posy +20
            self.pos_to_grid()
            self.add(plot=True)
            sleep(0.05)

    def end_fall(self):
        ok = False
        for i in range(len(self.geometry)):
            for j in range(len(self.geometry[i])):
                if self.geometry[i][j] == 1:
                    if self.board.config[self.gridy+i+1][self.gridx+j][0] == 'W':
                        ok = True
                else:
                    pass
        if ok:
            combo = 0
            for i in range(len(self.board.config)-1):
                for j in range(len(self.board.config[i])):
                    if self.board.config[i][j][0] == 'B':
                        self.board.config[i][j] = 'W'+ self.board.config[i][j][-1]
                if sorted(self.board.config[i])[0][0] == 'W':
                    for block in range(1,len(self.board.config[i])-1):
                        self.screen.blit(self.back,(gtpx(block),gtpy(i)))
                    self.erase_line(i)
                    combo = combo + 1
                    ligne = self.board.config.pop(i)
                    self.board.config.insert(0,ligne)
            self.scoreboard.increase(self.scoreboard.dictcombo[combo])

        return ok


def gtpx(x):
    return x*20+160

def gtpy(y):
    return y*20+80


class Tetri_I(Tetriminos):
    def __init__(self,name,posx,posy,ecran, plat, scoreboard):
        Tetriminos.__init__(self, name, posx, posy, ecran, plat, scoreboard)
        self.color = 'C'
        self.type = 'I'
        self.geometry = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.orientations = [[[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
                             [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
                             [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
                             [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]]


class Tetri_O(Tetriminos):
    def __init__(self,name,posx,posy,ecran, plat, scoreboard):
        Tetriminos.__init__(self, name, posx, posy, ecran, plat, scoreboard)
        self.color = 'Y'
        self.type = 'O'
        self.geometry = [[1,1],[1,1]]

    def rotate(self):
        pass

class Tetri_T(Tetriminos):
    def __init__(self,name,posx,posy,ecran, plat, scoreboard):
        Tetriminos.__init__(self, name, posx, posy, ecran, plat, scoreboard)
        self.color = 'P'
        self.type = 'T'
        self.geometry = [[1,1,1],[0,1,0]]
        self.orientations = [[[0,0,0],[1,1,1],[0,1,0]],
                             [[0,1,0],[1,1,0],[0,1,0]],
                             [[0,1,0],[1,1,1],[0,0,0]],
                             [[0,1,0],[0,1,1],[0,1,0]]]

class Tetri_L(Tetriminos):
    def __init__(self,name,posx,posy,ecran, plat, scoreboard):
        Tetriminos.__init__(self, name, posx, posy,ecran, plat, scoreboard)
        self.color = 'O'
        self.type = 'L'
        self.geometry = [[1,1,1],[1,0,0]]
        self.orientations = [[[0,0,0],[1,1,1],[1,0,0]],
                             [[1,1,0],[0,1,0],[0,1,0]],
                             [[0,0,1],[1,1,1],[0,0,0]],
                             [[0,1,0],[0,1,0],[0,1,1]]]

class Tetri_J(Tetriminos):
    def __init__(self,name,posx,posy,ecran, plat, scoreboard):
        Tetriminos.__init__(self, name, posx, posy,ecran, plat, scoreboard)
        self.color = 'B'
        self.type = 'J'
        self.geometry = [[1,1,1],[0,0,1]]
        self.orientations = [[[0,0,0],[1,1,1],[0,0,1]],
                             [[0,1,0],[0,1,0],[1,1,0]],
                             [[1,0,0],[1,1,1],[0,0,0]],
                             [[0,1,1],[0,1,0],[0,1,0]]]

class Tetri_Z(Tetriminos):
    def __init__(self,name,posx,posy,ecran, plat, scoreboard):
        Tetriminos.__init__(self, name, posx, posy,ecran, plat, scoreboard)
        self.color = 'R'
        self.type = 'Z'
        self.geometry = [[1,1,0],[0,1,1],[0,0,0]]
        self.orientations = [[[1,1,0],[0,1,1],[0,0,0]],
                             [[0,0,1],[0,1,1],[0,1,0]],
                             [[0,0,0],[1,1,0],[0,1,1]],
                             [[0,1,0],[1,1,0],[1,0,0]]]

class Tetri_S(Tetriminos):
    def __init__(self,name,posx,posy,ecran, plat, scoreboard):
        Tetriminos.__init__(self, name, posx, posy,ecran, plat, scoreboard)
        self.color = 'G'
        self.type = 'S'
        self.geometry = [[0,1,1],[1,1,0],[0,0,0]]
        self.orientations = [[[0,1,1],[1,1,0],[0,0,0]],
                             [[0,1,0],[0,1,1],[0,0,1]],
                             [[0,0,0],[0,1,1],[1,1,0]],
                             [[1,0,0],[1,1,0],[0,1,0]]]


if __name__=='__main__':
    bloc = Tetri_T('a',0,0)
    print("\n")
    bloc.__repr__()
    print("\n")
    bloc.rotate()
    bloc.__repr__()
    print("\n")
    bloc.rotate()
    bloc.__repr__()
    print("\n")
    bloc.rotate()
    bloc.__repr__()
    print("\n")
    bloc.rotate()
    bloc.__repr__()
    print("\n")
    bloc.rotate()



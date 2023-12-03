import pygame


class ScoreBoard:
    def __init__(self,ecran):
        self.font = pygame.font.SysFont("monospace" ,30)
        self.text_score = self.font.render('Score : 0', 1, (255,255,255))
        self.text_record = self.font.render('Record : 0', 1, (255,255,255))
        self.background = pygame.image.load(r'textures/background.png').convert()
        self.screen = ecran
        self.score = 0
        record_file = open('record.txt','r')
        for i in record_file:
            self.record = int(i)
        record_file.close()
        self.dictcombo = {0: 0, 1: 40, 2: 100, 3: 300, 4: 1200}

    def __repr__(self):
        return f'Score : {self.score} / Record : {self.record}'

    def plot(self):
        if self.score>self.record:
            self.record = self.score
        self.text_score = self.font.render(f'Score : {self.score}', 1, (255,255,255))
        self.text_record = self.font.render(f'Record : {self.record}', 1, (255,255,255))
        self.screen.blit(self.background,(550,80))
        self.screen.blit(self.text_score,(550,80))
        self.screen.blit(self.text_record,(550,120))
        pygame.display.flip()

    def increase(self,point):
        self.score = self.score+point
        self.plot()

    def update_record(self):
        self.record = self.score
        self.plot()

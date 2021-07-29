import pygame
import time
import random
import string
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
class Balloon:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.color=(25,74,150)
        self.letter=random.choice(string.ascii_lowercase)
        self.size=50
        self.image=pygame.image.load('balloon.png')
       
        self.image=pygame.transform.rotozoom(self.image,0,0.2)
        self.text=font.render(self.letter, 1, (255,255,255))
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
        self.y=self.y-2
        if self.y<=0:
            self.reset()
        screen.blit(self.text,(self.x+40,self.y+40))
    def reset(self):
        self.x=random.randint(0,550)
        self.y=random.randint(600,700)
        self.letter=random.choice(string.ascii_lowercase)
        self.text=font.render(self.letter,1,(255,255,255))
font=pygame.font.SysFont('Times New Roman', 30)        
b=[]
for loop in range(0,5,1):
    x=random.randint(0,550)
    y=random.randint(600,700)
    b.append(Balloon(x,y))

screen.fill((0,0,0))
score=0
crash=pygame.image.load('StoppedWorking.png')
crash=pygame.transform.rotozoom(crash,0,0.5)
while True:
    scoretext=0

    scoretext=font.render(str(score),1,(142,194,15))

    screen.fill((0,0,0))

    for ball in b:
        
        ball.draw()
  
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            print(chr(event.key))
            for ball in b:
                if chr(event.key)==ball.letter:
                    ball.reset()
                    score=score+1
                    print(score)
    screen.blit(scoretext,(500,10))
    if score>=5:
        screen.blit(crash,(200,200))
        pygame.display.update()

        time.sleep(5)
        break
    pygame.display.update()

        
    

        

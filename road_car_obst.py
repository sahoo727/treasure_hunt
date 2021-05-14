import pygame
#from tkinter import *
#from pygame.locals import *
#import sys
#import os
import random
import math

#root = Tk()

#set uping
pygame.init()
l_x = 800
l_y = 600
screen = pygame.display.set_mode((l_x,l_y))
CLOCK = pygame.time.Clock()
pygame.display.set_caption('bg_scrl')
font = pygame.font.Font('freesansbold.ttf',20)
#FPS = 399


#img
global plr_x,plr_y,points,p_xch,p_ych
plyr_img = pygame.image.load('car_top1.png')
plr_x = 300
plr_y = 460
p_xch = 0
p_ych = 0
points = 0

class player:
    def __init__(self,image):
        self.image = image
        #self.plyr_rect = self.image.get_rect()

    def plyr(self,p_x,p_y):
        screen.blit(self.image,(p_x,p_y))

    #def ex(self,exm):


#bgimg
BG = pygame.image.load('road2.png')
'''
bkgd = pygame.image.load('road2.png').convert()
y_road = 0
pos=0
'''

#obstacle
#obstacles images
diamond1 = [pygame.image.load('diamond1.png'), pygame.image.load('diamond2.png'), 
        pygame.image.load('diamond3.png'), pygame.image.load('diamond4.png')]
diamond2 = [pygame.image.load('diamond1.png'), pygame.image.load('diamond2.png')]
diamond3 = [pygame.image.load('diamond7.png'), pygame.image.load('diamond4.png')]
diamond4 = [pygame.image.load('diamond5.png'), pygame.image.load('diamond6.png')]
obs_wall = [pygame.image.load('brickwall.png')]

#creating obst class
class obstacles:
    def __init__(self,image,type):
        #global collision
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = random.randint(140,550)
        #collision = 0
        #self.rect.y = rect.y
        if self == diamonds1:
            self.rect.y = random.randint(20,50)
            #collision = 1
            #self.rect.x = random.randint(370,550)
        elif self == diamonds2:
            self.rect.y = random.randint(100,160)
            #self.collision = 0
            #self.rect.x = random.randint(370,550)
        elif self == diamonds3:
            self.rect.y = random.randint(20,50)
            #self.collision = 0
            #self.rect.x = random.randint(430,550)
        elif self == diamonds4:
            self.rect.y = random.randint(100,170)
            #self.collision = 0
            #self.rect.x = random.randint(430,550)
            #menu()

    
    def update(self,plr_x,plr_y,obs):
        #self.rect.y = y_move
        #self.plr_img = image_plr.get_rect()
        #global points
        print('x',self.rect.x,plr_x)
        print('y',self.rect.y,plr_y)
        print()
        d=math.sqrt(pow(self.rect.x - plr_x , 2) + pow(self.rect.y - plr_y ,2))
        #z=player(plyr_img)

        self.rect.y += game_speed
        if self.rect.y > l_y:#self.rect.height :
            obs.pop()
        #if self.rect.x == plr_x and self.rect.y == plr_y:
        #    print(1)
        if d<=100:
            #print(1)
            #print('coll',collision)
            #if self.collision == 1:
            #    menu()
            
            pygame.draw.rect(screen,(255,0,0),self.rect,2)
            #print(self)
            obs.remove(self)
            coll = 1
            #points+=10
            #print(points)
            score(coll)
    
    def draw(self,screen):
        screen.blit(self.image[self.type], self.rect)

class obstacles2:
    def __init__(self,image,type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = random.randint(140,550)
        self.rect.y = random.randint(50,160)

    def update(self,plr_x,plr_y,obs):
        self.rect.y += game_speed
        if self.rect.y > l_y:
            obs.pop()

        d=math.sqrt(pow(self.rect.x - plr_x , 2) + pow(self.rect.y - plr_y ,2)) 
        if d<=100:
            #pygame.draw.rect(screen,(255,0,0),self.rect,2)
            #print(1)
            menu()
    
    def draw(self,screen):
        screen.blit(self.image[self.type],self.rect)


class diamonds1(obstacles):
    def __init__(self,image):
        self.type = random.randint(0,3)
        #self.rect.y = random.randint(20,130)
        super().__init__(image, self.type)
        #self.rect.y = random.randint(20,300)
        #self.rect.y = 25

    #obstacles.update()


class diamonds2(obstacles):
    def __init__(self,image):
        self.type = random.randint(0,1)
        #self.rect.y = random.randint(20,130)
        super().__init__(image, self.type)
        #self.rect.y = random.randint(20,300)
        #self.rect.y = 25

    #obstacles.update(y_move=25)

class diamonds3(obstacles):
    def __init__(self,image):
        self.type = random.randint(0,1)
        #self.rect.y = random.randint(170,300)
        super().__init__(image, self.type)
        #self.rect.y = random.randint(20,300)
        #self.rect.y = 25

    #obstacles.update(y_move=25)

class diamonds4(obstacles):
    def __init__(self,image):
        self.type = random.randint(0,1)
        #3self.rect.y = random.randint(170,300)
        super().__init__(image, self.type)
        #self.rect.y = random.randint(20,300)
        #self.rect.y = 25

    #obstacles.update(y_move=25)

class wall(obstacles2):
    def __init__(self,image):
        self.type = 0
        super().__init__(image,self.type)

    

def background():
    global x_pos_bg , y_pos_bg
    image_height = BG.get_height()
    screen.blit(BG,(x_pos_bg , y_pos_bg))
    screen.blit(BG, ( x_pos_bg , y_pos_bg - image_height ))
    if y_pos_bg >= l_y:
        screen.blit(BG, ( x_pos_bg , y_pos_bg - image_height ))
        y_pos_bg = -10
    y_pos_bg += game_speed


def score(coll):
    global points,game_speed
    if coll == 1:
        points += 10
    if points % 50 == 0:
        game_speed += 0.3
    
    text =font.render('Points : '+ str(points) , True , (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (550,20)
    screen.blit(text , text_rect)


def main():
    #main loop
    global game_speed, x_pos_bg , y_pos_bg,plr_x,plr_y,p_xch,p_ych
    x_pos_bg = 0
    y_pos_bg = 0
    play = player(plyr_img)
    game_speed = 10
    obs = []
    #points = 0
    run = True
    while run:
        screen.fill((255,255,255))

        #running road
        background()

        #quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

       
            '''
            rel_y = y_road % bkgd.get_rect().heightimage_height

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pos=rel_y-bkgd.get_rect().heightimage_height
                    screen.blit(bkgd,(0,pos))
                    if rel_y < 800:
                        pos=rel_y
                        screen.blit(bkgd,(0,pos))
                    y_road += 1
            ''' 
        
            #player changing rect.y (left right)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p_xch = -7
                if event.key == pygame.K_RIGHT:
                    p_xch = 7
                if event.key == pygame.K_UP:
                    p_ych = -7
                if event.key == pygame.K_DOWN:
                    p_ych = 7
            
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                    p_xch = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    p_ych = 0

        plr_x += p_xch
        plr_y += p_ych
        #boundary setting
        if plr_x <= 150:
            plr_x = 150
        if plr_x >= 600:
            plr_x = 600
        

        #on screen obstacles
        '''
        if len(obs) == 0:
            if random.randint(0,3) == 0:
                obs.append(diamond1(diamond1))
            elif random.randint(0,3) == 1:
                obs.append(diamond2(diamond2))
            elif random.randint(0,3) == 2:
                obs.append(diamond(diamond3))
            elif random.randint(0,3) == 3:
                obs.append(diamond(diamond4))
    '''    

        if len(obs) == 0:
            num = random.randint(0,2)
            if  num == 0:
                obs.append(diamonds1(diamond1))
                obs.append(diamonds3(diamond3))
            elif num == 1:
                obs.append(diamonds2(diamond2))
                obs.append(diamonds4(diamond4))
            elif num == 2:
                obs.append(wall(obs_wall))
        '''
            elif random.randint(0,3) == 2:
                obs.append(diamond(diamond3))
            elif random.randint(0,3) == 3:
                obs.append(diamond(diamond4))
        '''



        for obstacles in obs:
            obstacles.draw(screen)
            obstacles.update(plr_x, plr_y, obs)
            '''
            if play.plyr_rect.colliderect(obstacles.rect):
                pygame.draw.rect(screen,(255,0,0),play.plyr_rect,2)
                print(1)
                #pygame.quit()
            '''

        
        #player call
        play.plyr(plr_x,plr_y)
        print(plr_x,plr_y)
        score(0)
        #print(plr_x,plr_y)

        pygame.display.update()
        CLOCK.tick(10)
        #events()

    
#main()

def menu():
    global points
    run = True
    while run:
        screen.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf',20)
        
        if points == 0:
            text = font.render('Press Any Key To Start ',True,(0,0,0))
        elif points > 0:
            text = font.render('press any key t rol dice',True,(0,0,0))
            scores = font.render('Your score :'+str(points),True,(0,0,0))
            scoresRect = scores.get_rect()
            scoresRect.center = (l_x//2 , l_y//2+50)
            screen.blit(scores,scoresRect)

        textRect = text.get_rect()
        textRect.center = (l_x//2 , l_y//2)
        screen.blit(text , textRect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                #break
                                
            elif event.type == pygame.KEYDOWN:
                main()

menu()

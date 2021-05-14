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
obs_car = [pygame.image.load('obs_car1.png'), pygame.image.load('obs_car2.png'), 
        pygame.image.load('obs_car3.png'), pygame.image.load('obs_car4.png')]
obs_trk = [pygame.image.load('obs_truck1.png'), pygame.image.load('obs_truck2.png')]
obs_fire = [pygame.image.load('fire1.png'), pygame.image.load('fire2.png')]
obs_stone = [pygame.image.load('stone.png'), pygame.image.load('stone_fall.png')]


#creating obst class
class obstacles:
    def __init__(self,image,type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = random.randint(140,550)
        #self.rect.y = rect.y
        if self == car:
            self.rect.y = random.randint(20,50)
        elif self == truck:
            self.rect.y = random.randint(100,160)
        elif self == stone:
            self.rect.y = random.randint(20,50)
        elif self == fire :
            self.rect.y = random.randint(100,170)

    
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
            print(1)
            pygame.draw.rect(screen,(255,0,0),self.rect,2)
            obs.remove(self)
            coll = 1
            #points+=10
            #print(points)
            score(coll)
    
    def draw(self,screen):
        screen.blit(self.image[self.type], self.rect)


class car(obstacles):
    def __init__(self,image):
        self.type = random.randint(0,3)
        #self.rect.y = random.randint(20,130)
        super().__init__(image, self.type)
        #self.rect.y = random.randint(20,300)
        #self.rect.y = 25

    #obstacles.update()


class truck(obstacles):
    def __init__(self,image):
        self.type = random.randint(0,1)
        #self.rect.y = random.randint(20,130)
        super().__init__(image, self.type)
        #self.rect.y = random.randint(20,300)
        #self.rect.y = 25

    #obstacles.update(y_move=25)

class fire(obstacles):
    def __init__(self,image):
        self.type = random.randint(0,1)
        #self.rect.y = random.randint(170,300)
        super().__init__(image, self.type)
        #self.rect.y = random.randint(20,300)
        #self.rect.y = 25

    #obstacles.update(y_move=25)

class stone(obstacles):
    def __init__(self,image):
        self.type = random.randint(0,1)
        #3self.rect.y = random.randint(170,300)
        super().__init__(image, self.type)
        #self.rect.y = random.randint(20,300)
        #self.rect.y = 25

    #obstacles.update(y_move=25)

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
    game_speed = 13
    obs = []
    #points = 0
    run = True
    while run:
        screen.fill((255,255,255))
        #quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        #running road
        background()
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
                obs.append(car(obs_car))
            elif random.randint(0,3) == 1:
                obs.append(truck(obs_trk))
            elif random.randint(0,3) == 2:
                obs.append(fire(obs_fire))
            elif random.randint(0,3) == 3:
                obs.append(stone(obs_stone))
    '''    

        if len(obs) == 0:
            if random.randint(0,1) == 0:
                obs.append(car(obs_car))
                obs.append(fire(obs_fire))
            elif random.randint(0,1) == 1:
                obs.append(truck(obs_trk))
                obs.append(stone(obs_stone))
        '''
            elif random.randint(0,3) == 2:
                obs.append(fire(obs_fire))
            elif random.randint(0,3) == 3:
                obs.append(stone(obs_stone))
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

    
main()


from __future__ import division
import math
import sys
import pygame
import random
import time

class Orange(object):
    def __init__(self, position, image):
        self.image = image
        self.position = [random.randint(350, 550), random.randint(400, 570)]  

    def draw(self, surface):
        surface.blit(self.image, self.position)  


class Witch(object):
    def __init__(self, position, image, speed):

        self.image = image
        self.speed = speed
        
        self.position = [random.randint(0, 760), random.randint(0, 150)]       
        self.destination = (random.randint(350, 550), random.randint(410, 570)) 

        


    def draw(self, surface):
        #vector for position of witches

        v = (self.destination[0] - self.position[0], self.destination[1]-self.position[1])
        n = math.sqrt(v[0]**2 + v[1]**2)
        uv = v[0]/n, v[1]/n
        
        self.position[0] += uv[0]*self.speed
        self.position[1] += uv[1]*self.speed
                       
        surface.blit(self.image, self.position)


        
class MyGame(object):
    def __init__(self):
        """Initialize a new game"""
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        # set up a window
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))

        #load images
        self.orange = pygame.image.load('orange.png')
        self.witch = pygame.image.load('witchs.png')

        #load soundes
        self.shoot = pygame.mixer.Sound('shoot.wav')
        self.sad = pygame.mixer.Sound('over.wav')
        self.nom = pygame.mixer.Sound('nom.wav')
        self.sound = pygame.mixer.Sound('sound1.wav')
        self.sound.set_volume(0.2)




        # use a nixe background
        self.bg_color = 245, 245, 220

        # Setup a timer to refresh the display FPS times per second
        self.FPS = 30
        self.REFRESH = pygame.USEREVENT+1
        pygame.time.set_timer(self.REFRESH, 1000//self.FPS)
        self.timer = 0
        self.timer2 = 0 
        self.game_over = False
        self.first_time = 0
        
        self.score = 0
        
        if self.first_time == 0:
            self.best_score = self.score

        self.lives = 5
        
        #font and text
        font = pygame.font.Font('CALLIGRA.TTF', 50)
        text = "WELCOME TO MY GAME" 
        fontColor = (255, 127, 36)
        self.fontim = font.render(text, 0, fontColor)
        
        self.position_random = [random.randint(0, 760), random.randint(0, 80)]
             


        self.startposition = [random.randint(0, 760), random.randint(0, 50)]   
        
        self.oranges = []  
        for x in xrange(30):
            position = self.width//2, self.height//2
            self.oranges.append(Orange(position, self.orange))
        self.speed = 3
        self.witches = []  
        for x in xrange(3):
            position = self.width//2, self.height//2
            self.witches.append(Witch(position, self.witch, self.speed))

        self.pos = 0, 0
        self.play = True
        self.timer3 = 0
        self.count = 0


    def run(self):
        """Loop forever processing events"""
        running = True
        while running:
            event = pygame.event.wait()
            
            # player is asking to quit
            if event.type == pygame.QUIT:
                running = False
            
            

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.pos = pygame.mouse.get_pos()
                if self.game_over == True and self.timer2 >= 80:
                    MyGame().run()
                    pygame.quit
                    sys.exit()  
                
            # time to draw a new frame    
            elif event.type == self.REFRESH:
                #self.sound.play()

                self.timer += 1
                if self.play == False:
                    
                    self.timer3 += 1
                
                if self.timer3 == 30:
                    self.play = True
                    self.timer3 = 0
                        

                if self.game_over == True:
                    self.timer2 += 1    
                    self.first_time +=4


                self.draw()

            else:
                pass # an event type we don't handle            

    def draw(self):
        """Update the display"""
        # everything we draw now is to a buffer that is not displayed
        self.screen.fill(self.bg_color)
        self.position_for_few = self.position_random
        self.eaten_oranges = []
        font1 = pygame.font.Font('BOOMERAN.TTF', 120)
        
        text1 = "GAME OVER!"
        fontColor1 = (205, 0, 0)
        self.fontim1 = font1.render(text1, 0, fontColor1)
        
        text2 = "You score is %r" % self.score
        self.fontim4 = font1.render(text2, 0, fontColor1)
        
        text3 = "Click to play a new game"
        self.fontim5 = font1.render(text3, 0, fontColor1)
        


        font2 = pygame.font.Font('ADLER.TTF', 20)
        text2 = "Lives: %r" % self.lives
        fontColor2 = (255, 127, 36)
        self.fontim2 = font2.render(text2, 0, fontColor2)
        
        text3 = "Score: %r" % self.score
        self.fontim3 = font2.render(text3, 0, fontColor2)

        text4 = "The best score is %r" % self.best_score
        self.fontim6 = font2.render(text4, 0, fontColor1)

        

       
        if 1 < self.timer < 30:
            rect = self.fontim.get_rect()
            rect = rect.move((self.width-rect.width)//2, (self.height-rect.height)//2)
            self.screen.blit(self.fontim, rect)
            
        if self.game_over == False and self.play == True:         
            if self.timer > 30:
                for i in self.oranges:
                    i.draw(self.screen)
            

                
                for witch in self.witches:  
                                        
                    
                    witch.draw(self.screen)
                    witch_x = witch.position[0]
                    witch_y = witch.position[1]                
                

        
                    if 350 <= int(witch_y) < 550:
                        for o in self.oranges:
                            self.nom.play()
                            self.oranges.remove(o)
                    


                    if self.pos[0] in range(int(witch_x)-35, int(witch_x)+35) and \
                                        self.pos[1] in range(int(witch_y)-40, int(witch_y)+40) :
                        self.shoot.play()
                        self.witches.remove(witch)
                        self.score += 5
                        position = self.position_for_few
                        self.witches.append(Witch(position, self.witch, self.speed))
                        witch.draw(self.screen)    

                    if len(self.oranges) == 0:
                        self.lives -= 1
                        self.witches = []
                        self.play = False
                        

                        for x in xrange(40):
                            self.oranges.append(Orange(self.pos, self.orange))
                        
                        for x in xrange(3):
                            self.speed = 4
                            self.witches.append(Witch(self.pos, self.witch, self.speed))

                        self.eaten_oranges = []   

                if self.lives ==  0:
                    self.game_over = True         
          
            self.screen.blit(self.fontim2, (5, 20))
            self.screen.blit(self.fontim3, (5, 50))   
            self.screen.blit(self.fontim6, (5, 80))                 
        
        if self.score >= 40:
            if len(self.witches) <= 4:
                position = self.position_for_few
                self.witches.append(Witch(position, self.witch, self.speed)) 

        if self.score >= 80:
            if len(self.witches) <= 6:
                speed = 4
                position = self.position_for_few
                self.witches.append(Witch(position, self.witch, speed))
                self.witches.append(Witch(position, self.witch, speed)) 
        if self.score >= 130:
            if len(self.witches) <= 8:
                for witch in self.witches:
                    witch.speed = 5

                                                     
        
        if self.game_over == True:
            self.play = False
            self.sad.play()
            if self.score >= self.best_score:
                self.best_score = self.score
                         
            rect1 = self.fontim1.get_rect()
            rect1 = rect1.move((self.width-rect1.width)//2, (self.height-rect1.height)//2)
            self.screen.blit(self.fontim1, rect1)
            self.screen.blit(self.fontim4, (280, 350)) 
            self.screen.blit(self.fontim5, (100, 80))
            self.screen.blit(self.fontim6, (5, 80))
                    

                        
                




            
        # flip buffers so that everything we have drawn gets displayed
        pygame.display.flip()

MyGame().run()
pygame.quit()
sys.exit()

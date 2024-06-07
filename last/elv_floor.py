import time
import pygame
from my_setting import *



class elv:

    def __init__(self , num ,elv_img) -> None:
        self.num_elv = num
        self.total_time = 0
        self.last_update_time = time.time() 
        self.y_position = START_Y_POS_FLOOR  
        self.x_position = num * 50 + 150
        self.list_req = []
        self.puse = 0
        self.img = pygame.transform.scale(elv_img , (50,50))
        self.where_m_i = 0
        self.mp3 = pygame.mixer.Sound("ding.mp3")
        

    def get_new_req(self, new_floor):

        if not self.list_req:
            self.list_req.append(self.where_m_i)
             
        size = len(self.list_req ) - 1
        last_req = self.list_req[size]

        dist = abs(last_req - new_floor) 
        self.total_time += (dist * SECONDES_FOR_FLOOR) + 2
        self.list_req.append(new_floor)
        
    
    def update_elv(self ):
        #update total time
        diff = time.time() - self.last_update_time 
        pixels_per_sec = HEIGHT_FLOOR / SECONDES_FOR_FLOOR
        distance = diff * pixels_per_sec
        
        self.last_update_time = time.time()
        
        if self.total_time >= 0.01:
            self.total_time -= diff
        else:
            self.total_time = 0

        #update the y_position the high of the elv
        if not self.list_req:
            self.list_req.append(self.where_m_i)
       
        if self.list_req:   
            num_floor = self.list_req[0] 
        
            y_floor = START_Y_POS_FLOOR - (num_floor * HEIGHT_FLOOR) 
             
            # if is not in the dest pix go to
            if int(self.y_position) != int(y_floor):
                self.puse = 2
                #go to y_floor pix 
                if self.y_position > y_floor:
                    self.y_position -= distance
                elif self.y_position < y_floor:
                    self.y_position  += distance
           
            # white 2 second 
            elif self.puse > 0: 
                if self.puse == 2:
                    self.mp3.play()   
                self.puse -= diff

            # exit the last req and move the naxt  
            else:                  
                # self.puse = 0
                self.where_m_i = self.list_req.pop(0)           
        
                
#---------------------------------------------------------

class floor:
    def __init__(self, num) -> None:
        self.num_floor = num
        self.y_position = START_Y_POS_FLOOR - (num * HEIGHT_FLOOR)
        self.col_press = BLACK
        self.timer = 0
        self.last_update = time.time()
        self.timer_print = " "
        
    def update_floor(self):
        diff = time.time() - self.last_update
        self.last_update = time.time()

        if (self.timer) > 0.001:
            self.timer -= diff
        else:
            self.col_press = BLACK
        self.convert_timer_to_str()

    def convert_timer_to_str(self):
        #convert to string for print the timer in text xx:yy
        integ = int(self.timer)
        dicimal = (self.timer - integ)
        integ = str(integ)
        dicimal = str(dicimal)
        self.timer_print = integ + '.'  + dicimal[2:4]


        


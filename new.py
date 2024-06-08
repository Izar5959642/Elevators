import pygame
from my_setting import *
import time


class Elv:
    def __init__(self,num_elv , elv_img) -> None:
        self.num_elv =  num_elv
        self.x_pos = START_X_POS_ELV + (DIFF_ELV * num_elv)
        self.y_pos = ZERO_FLOOR
        self.where_m_i = 0
        self.total_time = 0
        self.last_update_time = time.time()
        self.list_req = []
        self.final_dest = 0
        self.img = pygame.transform.scale(elv_img , (ELV_WIDTH,ELV_HEIGHT))
        self.puse = 0
        self.mp3 = pygame.mixer.Sound(MP3)


    def appendReq(self, num_floor , new_total_time):
        #update final dest
        #update list req
        #update final_dest

        self.list_req.append(num_floor)
        self.total_time = new_total_time
        self.final_dest = num_floor

    def calculateTimeForNewReq(self, num_floor):
        diff = abs(self.final_dest - num_floor) * SEC_FOR_FLOOR
        final_time = diff + self.total_time 
        return final_time
        
    def upDate(self):
        #update time 
        diff = time.time() - self.last_update_time
        self.last_update_time = time.time()

        if self.total_time >= 0.01:
            self.total_time -= diff
        else:
            self.total_time = 0

        #if there no req = the elv stand
        if not self.list_req:
            return
        
        distance = PIX_PER_SEC * diff

        current_dest = self.list_req[0]
        y_floor = ZERO_FLOOR - (FLOOR_HEIGHT * current_dest)

        if int(self.y_pos) != int(y_floor):
            self.puse = 2
            if self.y_pos > y_floor:
                self.y_pos -= distance

            elif self.y_pos < y_floor:
                self.y_pos += distance
        
        #wait 2 second
        elif self.puse > 0:  
            if self.puse == 2:
                  self.mp3.play()
            self.puse -= diff
        else:
            self.where_m_i = self.list_req.pop(0)   
        return

# --------------------------------------
class Floor:
    def __init__(self , num_floor,elv_img) -> None:
        self.num_elv = num_floor
        self.x_pos = START_X_POS_FLOOR
        self.y_pos = ZERO_FLOOR - (FLOOR_HEIGHT * num_floor) 
        self.timer = 0
        self.timer_str = ''
        self.img = pygame.transform.scale(elv_img, (FLOOR_WIDTH, FLOOR_HEIGHT - LINE_DIFF))
        self.col_num = BLACK
        self.last_update = time.time()


    def upDate(self):
        diff = time.time() - self.last_update
        self.last_update = time.time()

        if self.timer > 0:
            self.timer -= diff
        else:
            self.col_num = BLACK
        self.convertTimeStr()
 
    def convertTimeStr(self):
        int_timer = int(self.timer)
        dicimal_timer = (self.timer - int_timer)
        int_timer = str(int_timer)
        dicimal_timer = str(dicimal_timer)
        self.timer_str = int_timer + '.' + dicimal_timer[2:4]

#--------------------------------
class Building:
    def __init__(self, NUM_ELV, NUM_FLOORS) -> None:
        self.img_elv = pygame.image.load(IMG_ELV)
        self.img_floor = pygame.image.load(IMG_FLOOR)
        self.elevators = []
        self.floors = []

        #init elv 
        for i in range(NUM_ELV):
            self.elevators.append(Elv(i, self.img_elv))
        #init floors
        for i in range(NUM_FLOORS):
            self.floors.append(Floor(i, self.img_floor))
        
    def getNewReq(self, num_floor):

        # if floor alrady press skip on the req
        if self.floors[num_floor].col_num == GREEN:
            return
        #mini is touple of num of (min_time, num_elv )
        mini = [float('inf') , 0]

        #for on all the elv to find the min elv to get the req floor
        for i in range(NUM_ELV):
            time_elv_get_floor = self.elevators[i].calculateTimeForNewReq(num_floor)
            if mini[0] > time_elv_get_floor:
                mini[0] = time_elv_get_floor
                mini[1] = i

        #sand to the min elv, and setup floor_timer and floor_color
        if self.floors[num_floor].col_num == BLACK:
            self.elevators[mini[1]].appendReq(num_floor,mini[0] + 2)
           
            self.floors[num_floor].timer = mini[0]
            self.floors[num_floor].col_num = GREEN
        return
    
    def updateAll(self):
        for i in range(NUM_ELV):
            self.elevators[i].upDate()
        for i in range(NUM_FLOORS):
            self.floors[i].upDate()      
        



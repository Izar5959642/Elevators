import pygame
from my_setting import *
import time


#
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

    # the elevator get new request
    def appendReq(self, num_floor , new_total_time):
        '''''
        
        '''''
        #update final dest, update list req, update final_dest
        self.list_req.append(num_floor)
        self.total_time = new_total_time
        self.final_dest = num_floor


    #returen final time for floor request
    def calculateTimeForNewReq(self, num_floor):
        # if the elevator allredy in the floor request  
        if self.final_dest == num_floor:
            return 0
        diff = abs(self.final_dest - num_floor) * SEC_FOR_FLOOR 
        final_time = diff + self.total_time 
        return final_time
    
    # main update of elv
    def update(self):

        #update time 
        diff = time.time() - self.last_update_time
        self.last_update_time = time.time()
        self.updateTotalTime(diff)

        # update x,y position:
        #if there  is request move elv, else: (no req) = the elv stand
        if  self.list_req:
            self.move(diff)
        return
    

    def updateTotalTime(self,diff):
        '''''
        diff = current_time - last_update_time 
        the function update total_time if needed
        '''''
        
        if self.total_time >= 0.01:
            self.total_time -= diff
        else:
            self.total_time = 0

    def move(self , diff):
        '''''
        diff = current_time - last_update_time 
        the function update y_pos of elevator if needed 
        '''''
        # get the current dest from the head list and calculate the y floor 
        current_dest = self.list_req[0]
        y_floor = ZERO_FLOOR - (FLOOR_HEIGHT * current_dest)
        distance = PIX_PER_SEC * diff

        # move y_elv to y_floor    
        if self.y_pos != y_floor: 
            # useing where_m_i for understandig if the elevator move up or down
            # if the movement is up 
            if self.where_m_i < current_dest:
                if self.y_pos > y_floor:
                    self.y_pos -= distance 
                else:
                    self.y_pos = y_floor
                    self.puse = PUSE
            # if the movement is down
            elif self.where_m_i > current_dest:
                if self.y_pos < y_floor:
                    self.y_pos += distance
                else:
                    self.y_pos = y_floor
                    self.puse = PUSE
        # when the y_elv == y_floor, arrive to the floor 
        elif self.puse > 0:  
            if self.puse == PUSE:
                  self.mp3.play()
            self.puse -= diff
            self.y_pos = y_floor
        else:
            # after two sec waiting remove the floor request from list_req 
            # and keep the floor for understanding move up or down
            self.where_m_i = self.list_req.pop(0)   
        return
    

    def draw(self,screen):
        screen.blit(self.img, (self.x_pos ,self.y_pos) )

#---------------------------------------
class Button:
    def __init__(self, num_button, y_pos, img_floor_rect) -> None:
        self.x_pos = X_START_POS_BUTTON
        self.y_pos = y_pos + (FLOOR_HEIGHT / 2)
        self.background = BG
        self.col_button = COL_BUTTON_OFF
        self.font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTON_NUM)
        self.button_press = False
        self.str_num_floor = str(num_button)
        self.text_button = self.font.render( self.str_num_floor, True, self.col_button, self.background)
        self.rect = self.text_button.get_rect(center=(self.x_pos, self.y_pos))
        
    # check if x,y pos mouse is in the range of the button
    def checkPress(self,x_mouse,y_mouse):
        if  not x_mouse in range(int(X_START_POS_BUTTEN_CLICK), int(X_END_POS_BUTTEN)) :
            return False
        if y_mouse in range(int(self.y_pos - SIZE_BUTTON),int( self.y_pos + SIZE_BUTTON)):
            return True
        else:
            return False
    

    def update(self , button_press ):
        if button_press == True:
            self.button_press = True
            self.col_button = COL_BUTTON_ON
        else:
            self.button_press = False
            self.col_button = COL_BUTTON_OFF
        self.text_button = self.font.render( self.str_num_floor, True, self.col_button, self.background)
        
    def draw(self, screen, img_floor_rect):
        x = self.x_pos  
        y = self.y_pos 
        
        pygame.draw.circle(screen, (BG), ( x,y), SIZE_BUTTON )
        pygame.draw.circle(screen, (BLACK), ( x,y), SIZE_BUTTON , 3)
        
        screen.blit(self.text_button, self.text_button.get_rect(center=(x, y)))


# --------------------------------------
class Floor:
    def __init__(self , num_floor,floor_img) -> None:
        self.num_floor = num_floor
        self.x_pos = START_X_POS_FLOOR
        self.y_pos = ZERO_FLOOR - (FLOOR_HEIGHT * num_floor) 
        self.timer = 0
        self.timer_str = ''
        self.img = pygame.transform.scale(floor_img, (FLOOR_WIDTH, FLOOR_HEIGHT - LINE_DIFF))
        self.col_num = BLACK
        self.last_update = time.time()
        self.flag_in_execution= False
        self.font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTON)
        self.rect = self.img.get_rect(center=(self.x_pos, self.y_pos))

        self.button = Button(self.num_floor, self.y_pos, self.rect)


    def byOrder(self, time):
        self.timer = time
        self.col_num = GREEN
        self.flag_in_execution = True
        


    def update(self):
        diff = time.time() - self.last_update
        self.last_update = time.time()

        if self.timer > 0:
            self.timer -= diff
        else:
            self.col_num = BLACK
            self.flag_in_execution = False
        self.convertTimeStr()

        self.button.update(self.flag_in_execution)
 
    def convertTimeStr(self):
        int_timer = int(self.timer)
        dicimal_timer = (self.timer - int_timer)
        int_timer = str(int_timer)
        dicimal_timer = str(dicimal_timer)
        self.timer_str = int_timer + '.' + dicimal_timer[2:4]

    def draw(self, screen):

        screen.blit(self.img, (self.x_pos ,self.y_pos) )   
       
        if self.num_floor < NUM_LINE:
            pygame.draw.rect(screen, (BLACK), (self.x_pos  ,self.y_pos - LINE_DIFF , FLOOR_WIDTH, LINE_DIFF))
        else:
             pygame.draw.polygon(screen, BLACK, roof_vertices)

        if self.flag_in_execution:
            timer_print = self.timer_str
            text_timer = self.font.render(timer_print , True,BG,BLACK)
            screen.blit(text_timer, (X_POS_TIMER, self.y_pos  + 15))
        self.button.draw(screen , self.rect)

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
        
    # check if the press is on the button = True, get the request.
    def getMouseClickPos(self, x_pos_mouse, y_pos_mouse):

            for num_floor, floor in enumerate(self.floors):
                if floor.button.checkPress(x_pos_mouse, y_pos_mouse):
                    self.getNewReq(num_floor)


    def getNewReq(self, num_floor):
        # if floor alrady press skip on the req
        if self.floors[num_floor].flag_in_execution == True:
            return
        #mini is touple of num of (min_time, num_elv )
        mini = [float('inf') , 0]

        #for on all the elv to find the min elv to get the req floor
        for i ,elv in enumerate(self.elevators):
            time_elv_get_floor = elv.calculateTimeForNewReq(num_floor)
            if mini[0] > time_elv_get_floor:
                mini[0] = time_elv_get_floor
                mini[1] = i
       
        #sand to the min elv, and setup floor_timer and floor_color
        if self.floors[num_floor].flag_in_execution == False :
            self.elevators[mini[1]].appendReq(num_floor,mini[0] + PUSE)
            self.floors[num_floor].byOrder(mini[0])
        return
    
    def updateAll(self):
        for i in range(NUM_FLOORS):
            self.floors[i].update() 
        for i in range(NUM_ELV):
            self.elevators[i].update()

    def drawAll(self, screen):
        for elv in self.elevators:
            elv.draw(screen)
        for floor in self.floors:
            floor.draw(screen)
        
            
        # if x_pos_mouse in range(int(X_START_POS_BUTTEN_CLICK), int(X_END_POS_BUTTEN)) :
        
                # if y_pos_mouse >= floor.y_pos +10 and y_pos_mouse <= floor.y_pos + 50:
                    # print(floor.rect.left, floor.rect.right, floor.rect.top, floor.rect.bottom)
                    # print(x_pos_mouse, y_pos_mouse)



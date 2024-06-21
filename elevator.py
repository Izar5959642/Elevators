import pygame
from my_setting import *
import time

class Elv:
    """"
    The Elv class represents an elevator with methods to manage its movement and requests.

    Responsibilities:
    - Manage the elevator's position and movement.
    - Handle floor requests and calculate the time required to fulfill them.
    - Update the elevator's status and draw it on the screen.
    """""
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


    # Add a new request to the elevator.
    def appendReq(self, num_floor , new_total_time):
        '''''
        Add the requested floor to the list of requests and update the total time.
        Arguments:
            num_floor (int): The floor number to add to the request list.
            new_total_time (float): The new total time for the elevator to process the request.

        Returns:
            None
        '''''
        self.list_req.append(num_floor)
        self.total_time = new_total_time
        self.final_dest = num_floor


    # Calculate the time required for a new floor request.
    def calculateTimeForNewReq(self, num_floor):
        '''''
        Calculate and return the time needed for the elevator to reach the requested floor.
        Arguments:
            num_floor (int): The floor number for which the time is to be calculated.

        Returns:
            float: The time required for the elevator to reach the requested floor.
        '''''
        # If the elevator is already at the requested floor.
        if self.final_dest == num_floor:
            return 0
        diff = abs(self.final_dest - num_floor) * SEC_FOR_FLOOR 
        final_time = diff + self.total_time 
        return final_time
    
    # Main update function for the elevator.
    def update(self):
        '''
        Updates the elevator's position and time.
        Arguments:
            None
        Returns:
            None
        '''
        #Update time.
        diff = time.time() - self.last_update_time
        self.last_update_time = time.time()
        self.updateTotalTime(diff)
        # Update x and y position.       
        if  self.list_req:
            self.move(diff)
        return
    
    def updateTotalTime(self,diff):
        '''''
        Update the total time if needed.
        Arguments:
            diff (float): The time difference between the current time and the last update time.

        Returns:
            None
        '''''
        if self.total_time >= 0.01:
            self.total_time -= diff
        else:
            self.total_time = 0

    def move(self , diff):
        '''''
        Update the y position of the elevator if needed.
        Arguments:
            diff (float): The time difference between the current time and the last update time.

        Returns:
            None
        '''''
        # Get the current destination from the list and calculate the y position.
        current_dest = self.list_req[0]
        y_floor = ZERO_FLOOR - (FLOOR_HEIGHT * current_dest)
        distance = PIX_PER_SEC * diff
         # # Use where_m_i to understand if the elevator is moving up or down.
        direction = 1 if self.where_m_i > current_dest else -1
        distance *= direction
        if (self.y_pos) != (y_floor): 
        # Move the elevator to the y_floor.
            self.y_pos += distance
            if direction == 1 and self.y_pos > y_floor or direction == -1 and self.y_pos < y_floor:
                self.y_pos = y_floor 
                self.puse = PUSE


        # when the y_elv == y_floor, arrive to the floor .
        elif self.puse > 0:  
            if self.puse == PUSE:
                  self.mp3.play()
            self.puse -= diff
        else:
            # After waiting 2 sec, remove the floor request from the list and update where_m_i.
            self.where_m_i = self.list_req.pop(0)   
        return
    
    def draw(self,screen):
        '''''
        Draw the elevator image on the screen.
        Arguments:
            screen (pygame.Surface): The screen on which to draw the elevator image.

        Returns:
            None
       '''''
        screen.blit(self.img, (self.x_pos ,self.y_pos) )


            





           
            # if self.where_m_i < current_dest:
            #     if self.y_pos > y_floor:
            #         self.y_pos -= distance 
            #     else:
            #         self.y_pos = y_floor
            #         self.puse = PUSE
            # # If the movement is down
            # elif self.where_m_i > current_dest:
            #     if self.y_pos < y_floor:
            #         self.y_pos += distance
            #     else:
            #         self.y_pos = y_floor
            #         self.puse = PUSE
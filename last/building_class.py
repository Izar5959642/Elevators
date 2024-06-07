import pygame
from elv_floor import *
from my_setting import *



class Building:

    def __init__(self, num_elv, num_floors) -> None:
        self.elv_img = pygame.image.load(IMG_PATH)
        self.elv = []
        self.floors = []

        for i in range(num_elv):
            self.elv.append(elv(i,self.elv_img))
            
        for i in range(NUM_FLOORS):
            self.floors.append(floor(i))


    def get_request(self , num_floor):

        min = [float('inf') , 0]
        for i in range(NUM_ELV):

            if self.floors[num_floor].col_press == BLACK:
                if self.elv[i].list_req:
                    last_req = self.elv[i].list_req[len(self.elv[i].list_req) - 1]
                else:
                    last_req = self.elv[i].where_m_i

                distance = abs(last_req - num_floor) * SECONDES_FOR_FLOOR
                distance += self.elv[i].total_time
               
                if distance <= min[0]:
                    min[0] = (distance)
                    min[1] = i

        if self.floors[num_floor].col_press == BLACK:
            self.elv[min[1]].get_new_req(num_floor) 
            self.floors[num_floor].timer = self.elv[min[1]].total_time  - 2
            self.floors[num_floor].col_press = GREEN
            # self.floors[num_floor].arrived = 0
        
    def update_all(self):

        for i in range(NUM_ELV):
            self.elv[i].update_elv()
            
        for i in range(NUM_FLOORS):
            self.floors[i].update_floor()       

        
    
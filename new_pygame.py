import pygame
from my_setting import *
from building_floor_elv import *

#set the screen + the name window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Elevator Challenge')

# image background
img_background = pygame.image.load('/home/mefathim/Desktop/python/ws9_project/new_try/imegs/blackground.jpeg')
img_background = pygame.transform.scale(img_background, (SCREEN_WIDTH,SCREEN_HEIGHT))

# instance of building
my_building = Building(NUM_ELV,NUM_FLOORS)

run = True
while run:
    
    screen.blit(img_background, (0,0))
    my_building.updateAll()
    my_building.drawAll(screen)

    # exit mode
    pos_click_mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
        # get new reqeuste from the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            my_building.getMouseClickPos(pos_click_mouse[0], pos_click_mouse[1])
    pygame.display.update()

pygame.quit()


            # if pos_click_mouse[0] >= X_END_POS_BUTTEN_CLICK and pos_click_mouse[0] <= (X_END_POS_BUTTEN ):
            #     ckick_y_mous = pos_click_mouse[1] 
            #     for i in range(NUM_FLOORS):
            #         if pos_click_mouse[1] >= my_building.floors[i].y_pos +10 and pos_click_mouse[1] <= my_building.floors[i].y_pos + 50:
            #              my_building.getNewReq(i)
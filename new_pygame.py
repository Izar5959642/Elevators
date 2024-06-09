import pygame
from my_setting import *
from building_floor_elv import *

pygame.init()

#set the screen + the name window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('elvator project')

#create var img for elv and floor and font for num BUTTEN
img_elv = pygame.image.load(IMG_ELV).convert_alpha()
img_floor = pygame.image.load(IMG_FLOOR).convert_alpha()
font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTEN)

my_building = Building(NUM_ELV,NUM_FLOORS)
run = True


#get input from the mouse if he prees on the butten floor and sent to the building the requeste,
#print elevator ,timer , building , number butten .

while run:

    screen.fill(BG)
    #print elv img
    for i in range(NUM_ELV):
        screen.blit(my_building.elevators[i].img, (my_building.elevators[i].x_pos ,my_building.elevators[i].y_pos) )
    #print floor img include black line and roof
    for i in range(NUM_FLOORS):
        screen.blit(my_building.floors[i].img, (my_building.floors[i].x_pos ,my_building.floors[i].y_pos) )
        if i < NUM_LINE:
            pygame.draw.rect(screen, (BLACK), (my_building.floors[i].x_pos  ,my_building.floors[i].y_pos - LINE_DIFF , FLOOR_WIDTH, LINE_DIFF))
        else:
            pygame.draw.polygon(screen, BLACK, roof_vertices)

    for i in range(NUM_FLOORS):
        num  = str(i)
        text_num_floor = font.render( num, True, my_building.floors[i].col_num, BG) 
        if my_building.floors[i].col_num == GREEN:
            timer_print = my_building.floors[i].timer_str
            text_timer = font.render(timer_print , True,BG,BLACK)
            screen.blit(text_timer, (X_POS_TIMER, my_building.floors[i].y_pos  + 15))
        screen.blit(text_num_floor, (X_START_POS_BUTTEN, my_building.floors[i].y_pos  + 15))

    pos_click_mouse = pygame.mouse.get_pos()

    # exit mode
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos_click_mouse[0] >= X_START_POS_BUTTEN and pos_click_mouse[0] <= (X_END_POS_BUTTEN):
                for i in range(NUM_FLOORS):
                    if pos_click_mouse[1] >= my_building.floors[i].y_pos +15 and pos_click_mouse[1] <= my_building.floors[i].y_pos + 50:
                         my_building.getNewReq(i)

    my_building.updateAll()
    pygame.display.update()
    
pygame.quit()

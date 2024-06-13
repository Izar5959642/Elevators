import pygame
from my_setting import *
from building_floor_elv import *



# Initialize Pygame and set up the screen and window title.
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Elevator Challenge')

# Load and scale the background image.
img_background = pygame.image.load('/home/mefathim/Desktop/python/ws9_project/new_try/imegs/blackground.jpeg')
img_background = pygame.transform.scale(img_background, (SCREEN_WIDTH,SCREEN_HEIGHT))

# Create an instance of the Building class.
my_building = Building(NUM_ELV,NUM_FLOORS)

# Main loop flag.
run = True
while run:
    # Draw the background image.
    screen.blit(img_background, (0,0))
    # Update and draw all elevators and floors in the building.
    my_building.updateAll()
    my_building.drawAll(screen)

    # Get the current mouse position.
    pos_click_mouse = pygame.mouse.get_pos()
    # Event handling loop.
    for event in pygame.event.get():
        # Handle the quit event to exit the program.
        if event.type == pygame.QUIT:
            run = False
     
        # Handle mouse button down event to register new requests.
        if event.type == pygame.MOUSEBUTTONDOWN:
            my_building.getMouseClickPos(pos_click_mouse[0], pos_click_mouse[1])
    # Update the display.
    pygame.display.update()
# Quit Pygame.
pygame.quit()


            # if pos_click_mouse[0] >= X_END_POS_BUTTEN_CLICK and pos_click_mouse[0] <= (X_END_POS_BUTTEN ):
            #     ckick_y_mous = pos_click_mouse[1] 
            #     for i in range(NUM_FLOORS):
            #         if pos_click_mouse[1] >= my_building.floors[i].y_pos +10 and pos_click_mouse[1] <= my_building.floors[i].y_pos + 50:
            #              my_building.getNewReq(i)
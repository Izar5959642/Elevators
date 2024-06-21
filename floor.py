import pygame
from my_setting import *
import time
from pygame.locals import *


class Button:
    """
    The Button class represents a button in the elevator system.

    Responsibilities:
    - Manage the button's state (pressed or not pressed).
    - Check if the button has been pressed based on mouse position.
    - Update the button's appearance and draw it on the screen.
    """

    def __init__(self, num_button, y_pos) -> None:
        self.x_pos = X_START_POS_BUTTON
        self.y_pos = y_pos + (FLOOR_HEIGHT / 2)
        self.background = WHITE
        self.col_button = COL_BUTTON_OFF
        self.font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTON_NUM)
        self.button_press = False
        self.str_num_floor = str(num_button)
        self.text_button = self.font.render( self.str_num_floor, True, self.col_button, self.background)
        
    # Check if the x, y position of the mouse is in the range of the button.
    def checkPress(self,x_mouse,y_mouse):
        ''''
        Check if the mouse is over the button.
        Arguments:
            x_mouse (int): The x position of the mouse.
            y_mouse (int): The y position of the mouse.

        Returns:
            bool: True if the mouse is over the button, False otherwise.
        '''''
        if  not x_mouse in range(int(X_START_POS_BUTTEN_CLICK), int(X_END_POS_BUTTEN)) :
            return False
        if y_mouse in range(int(self.y_pos - SIZE_BUTTON),int( self.y_pos + SIZE_BUTTON)):
            return True
        else:
            return False
   
    # Update the button state based on whether it is pressed.
    def update(self , button_press ):
        ''''
        Update the button's state and coller button.
        Arguments:
            button_press (bool): True if the button is pressed, False otherwise.

        Returns:
            None
        '''''
        if button_press == True:
            self.button_press = True
            self.col_button = COL_BUTTON_ON
        else:
            self.button_press = False
            self.col_button = COL_BUTTON_OFF
        self.text_button = self.font.render( self.str_num_floor, True, self.col_button, self.background)

    # Draw the button on the screen.
    def draw(self, screen):
        '''''
        Draw the button on the screen.
        Arguments:
            screen (pygame.Surface): The screen on which to draw the button.

        Returns:
            None
        '''''
        pygame.draw.circle(screen, (WHITE), ( self.x_pos,self.y_pos), SIZE_BUTTON )
        pygame.draw.circle(screen, (BLACK), ( self.x_pos,self.y_pos), SIZE_BUTTON , 3)
        screen.blit(self.text_button, self.text_button.get_rect(center=(self.x_pos, self.y_pos)))

# Ciracal


# --------------------------------------
class Floor:
    """
    The Floor class represents a floor in the elevator system.

    Responsibilities:
    - Manage the floor's properties, such as position and timer.
    - Update the floor's state, including its timer and button state.
    - Draw the floor and its components on the screen.
    """

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
        # self.rect = self.img.get_rect(center=(self.x_pos, self.y_pos))

        self.button = Button(self.num_floor, self.y_pos)

    # Set the floor timer and update its state.
    def byOrder(self, time):
        """
        Set the floor's timer and mark it as active.
        Arguments:
            time (float): The time to set for the floor's timer.

        Returns:
            None
        """
        self.timer = time
        self.col_num = GREEN
        self.flag_in_execution = True
        

    # Update the floor's state, including the timer and button state.
    def update(self):
        """
        Update the floor's timer and button state.
        Arguments:
            None

        Returns:
            None
        """       
        diff = time.time() - self.last_update
        self.last_update = time.time()

        if self.timer > 0:
            self.timer -= diff
        else:
            self.col_num = BLACK
            self.flag_in_execution = False
        self.convertTimeStr()
        self.button.update(self.flag_in_execution)
 
    # Convert the timer to a string format.
    def convertTimeStr(self):
        """
        Convert the timer to a string format for display.
        Arguments:
            None

        Returns:
            None
        """
        int_timer = int(self.timer)
        dicimal_timer = (self.timer - int_timer)
        int_timer = str(int_timer)
        dicimal_timer = str(dicimal_timer)
        self.timer_str = int_timer + '.' + dicimal_timer[2:4]
  
    # Draw the floor and its components on the screen.
    def draw(self, screen):
        """
        Draw the floor, its dividing line, and its timer (if active) on the screen.
        Arguments:
            screen (pygame.Surface): The screen on which to draw the floor.

        Returns:
            None
        """
        # Print block image.
        screen.blit(self.img, (self.x_pos ,self.y_pos) )   
        # Draw black line between the floors; on the last floor, draw a roof.
        if self.num_floor < NUM_LINE:
            pygame.draw.rect(screen, (BLACK), (self.x_pos  ,self.y_pos - LINE_DIFF , FLOOR_WIDTH, LINE_DIFF))
        else:
             pygame.draw.polygon(screen, BLACK, roof_vertices)

        # If the floor has an active timer, draw the timer on the screen.
        if self.flag_in_execution:
            timer_print = self.timer_str
            text_timer = self.font.render(timer_print , True,WHITE,BLACK)
            screen.blit(text_timer, (X_POS_TIMER, self.y_pos  + 15))
        self.button.draw(screen)


        
            

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
        # Move the elevator to the y_floor.
        if self.y_pos != y_floor: 
            # Use where_m_i to understand if the elevator is moving up or down.
            # If the movement is up 
            if self.where_m_i < current_dest:
                if self.y_pos > y_floor:
                    self.y_pos -= distance 
                else:
                    self.y_pos = y_floor
                    self.puse = PUSE
            # If the movement is down
            elif self.where_m_i > current_dest:
                if self.y_pos < y_floor:
                    self.y_pos += distance
                else:
                    self.y_pos = y_floor
                    self.puse = PUSE
        # when the y_elv == y_floor, arrive to the floor .
        elif self.puse > 0:  
            if self.puse == PUSE:
                  self.mp3.play()
            self.puse -= diff
            # self.y_pos = y_floor<
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

#---------------------------------------
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

#--------------------------------
class Building:
    """
    The Building class represents the entire building, containing multiple elevators and floors.

    Responsibilities:
    - Initialize the elevators and floors.
    - Handle mouse click events to register floor requests.
    - Assign the best elevator for a floor request.
    - Update the state of all elevators and floors.
    - Draw all elevators and floors on the screen.
    """

    def __init__(self, NUM_ELV, NUM_FLOORS) -> None:
        self.img_elv = pygame.image.load(IMG_ELV)
        self.img_floor = pygame.image.load(IMG_FLOOR)
        self.elevators = []
        self.floors = []
      
        # Initialize elevators.
        for i in range(NUM_ELV):
            self.elevators.append(Elv(i, self.img_elv))
        # Initialize floors.
        for i in range(NUM_FLOORS):
            self.floors.append(Floor(i, self.img_floor))
        
    # Check if the mouse click is on any floor button, and handle the request if it is.
    def getMouseClickPos(self, x_pos_mouse, y_pos_mouse):
        """"
        Check if the mouse click is on a floor button and process the request.
        Arguments:
            x_pos_mouse (int): The x position of the mouse click.
            y_pos_mouse (int): The y position of the mouse click.

        Returns:
            None
        """""
        for num_floor, floor in enumerate(self.floors):
                if floor.button.checkPress(x_pos_mouse, y_pos_mouse):
                    self.getNewReq(num_floor)

    # Process a new floor request and assign it to the best elevator.
    def getNewReq(self, num_floor):
        """
        Process a new floor request and assign it to the best available elevator.
        Arguments:
            num_floor (int): The floor number where the request originated.

        Returns:
            None
        """
        # If the floor request is already in execution, skip it.
        if self.floors[num_floor].flag_in_execution == True:
            return
        # Find the elevator with the minimum time to fulfill the request.
        mini = [float('inf') , 0] # (min_time, num_elv)

        for i ,elv in enumerate(self.elevators):
            time_elv_get_floor = elv.calculateTimeForNewReq(num_floor)
            if mini[0] > time_elv_get_floor:
                mini[0] = time_elv_get_floor
                mini[1] = i
       
        # Assign the request to the best elevator and update the floor's state.
        if self.floors[num_floor].flag_in_execution == False :
            self.elevators[mini[1]].appendReq(num_floor,mini[0] + PUSE)
            self.floors[num_floor].byOrder(mini[0])
        return
    
    # Update the state of all elevators and floors.
    def updateAll(self):
        """
        Update the state of all elevators and floors.
        Arguments:
            None
        Returns:
            None
        """
        for i in range(NUM_FLOORS):
            self.floors[i].update() 
        for i in range(NUM_ELV):
            self.elevators[i].update()

    # Draw all elevators and floors on the screen.       
    def drawAll(self, screen):
        """
        Draw all elevators and floors on the screen.
        Arguments:
            screen (pygame.Surface): The screen on which to draw the elevators and floors.
        Returns:
            None
        """
        for elv in self.elevators:
            elv.draw(screen)
        for floor in self.floors:
            floor.draw(screen)
        
            

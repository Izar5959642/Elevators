import pygame
from my_setting import *
import time
from floor import *
from elevator import *



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
        
            

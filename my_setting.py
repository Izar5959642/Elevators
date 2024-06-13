# ! needed to keep the order of the line !

# 1. Colors
WHITE = (255, 255, 255)      # White color 
BLACK = (0, 0, 0)            # Black color
GREEN = (0, 255, 0)          # Green color

# 2. Screen
SCREEN_WIDTH = 1000          # Screen width
SCREEN_HEIGHT = 1000         # Screen height

# 3. Floor
FLOOR_WIDTH = 180            # Floor width
FLOOR_HEIGHT = 60            # Floor height
LINE_DIFF = 7                # Difference for line drawing
START_X_POS_FLOOR = 60      # Starting X position for floors
ZERO_FLOOR = SCREEN_HEIGHT - FLOOR_HEIGHT   # Y position of the ground floor
NUM_FLOORS = 15              # Number of floors
NUM_LINE = NUM_FLOORS - 1    # Number of lines between floors
SEC_FOR_FLOOR = 0.5          # Seconds it takes for an elevator to travel one floor
PIX_PER_SEC = FLOOR_HEIGHT / SEC_FOR_FLOOR  # Pixels per second an elevator travels
IMG_FLOOR = "/home/mefathim/Desktop/python/ws9_project/new_try/imegs/building.png"   # Image file for floors

# 4.1. Timer floor
X_POS_TIMER = START_X_POS_FLOOR + 5   # X position for the timer display on the floor

# 4.2. Button
SIZE_BUTTON = int(FLOOR_HEIGHT / 3)   # Size of the button
SIZE_BUTTON_NUM = SIZE_BUTTON         # Font size for the button number
X_START_POS_BUTTON = START_X_POS_FLOOR + (FLOOR_WIDTH) / 2  # X position for the button
MID_Y_POS = FLOOR_HEIGHT / 3          # Middle Y position for the button
X_END_POS_BUTTEN = X_START_POS_BUTTON + SIZE_BUTTON  # End X position for button click range
X_START_POS_BUTTEN_CLICK = X_START_POS_BUTTON - SIZE_BUTTON  # Start X position for button click range
COL_BUTTON_ON = GREEN                 # Color of the button when pressed
COL_BUTTON_OFF = BLACK                # Color of the button when not pressed

# 5. Elevator
START_X_POS_ELV = START_X_POS_FLOOR + FLOOR_WIDTH + 10  # Starting X position for elevators
ELV_WIDTH = 50                      # Elevator width
ELV_HEIGHT = FLOOR_HEIGHT - 10      # Elevator height
DIFF_ELV = ELV_WIDTH                # Difference in position between elevators
NUM_ELV = 3                         # Number of elevators
IMG_ELV = "/home/mefathim/Desktop/python/ws9_project/new_try/imegs/elv.png" # Image file for elevators
MP3 = "/home/mefathim/Desktop/python/ws9_project/new_try/mp3_file/ding.mp3"                    # Sound file for elevator arrival
PUSE = 2                            # Pause duration in seconds

# 6. Roof
UP_VERTICE = ZERO_FLOOR - (FLOOR_HEIGHT * NUM_FLOORS)  # Upper vertex of the roof
LEFT_RUGHT_Y_VERTICE = ZERO_FLOOR - (FLOOR_HEIGHT * (NUM_FLOORS - 1))  # Left and right vertices of the roof

# Ensure the upper vertex is not less than 0
if UP_VERTICE < 0:
    UP_VERTICE = 0

# Define the vertices of the roof polygon
roof_vertices = [
    ((START_X_POS_FLOOR + FLOOR_WIDTH) / 2, UP_VERTICE),
    (START_X_POS_FLOOR, LEFT_RUGHT_Y_VERTICE),
    (START_X_POS_FLOOR + FLOOR_WIDTH, LEFT_RUGHT_Y_VERTICE)
]


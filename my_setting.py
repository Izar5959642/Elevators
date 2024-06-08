
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

FLOOR_WIDTH = 175
FLOOR_HEIGHT = 60
LINE_DIFF = 7
START_X_POS_FLOOR = 20 

ELV_WIDTH = 50
ELV_HEIGHT = 50

ZERO_FLOOR = SCREEN_HEIGHT - 65
NUM_ELV = 5
NUM_FLOORS = 16
START_X_POS_ELV = 200
DIFF_ELV = 50


BG = (255,255,255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
 

SEC_FOR_FLOOR = .5
PIX_PER_SEC = FLOOR_HEIGHT / SEC_FOR_FLOOR 

IMG_ELV = "elv.png"
IMG_FLOOR = "building.png"
MP3 = "ding.mp3"


X_START_POS_BOTTEN = 90
SIZE_BOTTEN = 30
X_END_POS_BOTTEN = X_START_POS_BOTTEN + SIZE_BOTTEN
X_POS_TIMER = X_START_POS_BOTTEN + SIZE_BOTTEN + 15
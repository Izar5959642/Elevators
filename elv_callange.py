from elv_floor import *
from my_setting import *
from building_class import *
import pygame

pygame.init()

rect_b = pygame.Rect(RECTANGLE_SIZE)

font = pygame.font.Font('freesansbold.ttf', 50)
font_timer = pygame.font.Font('freesansbold.ttf' , 30)
text = font.render ('1', True, BLACK, BG) 
timer_floor = font_timer.render ('2', True, BLACK, BG)

textRect = text.get_rect()

#----------------------------------------------------------------------#

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('elv of Oltra Ortodux')

my_b = Building(NUM_ELV,NUM_FLOORS)

#----------------------------------------------------------------

run = True
while run:

    screen.fill(BLACK)

    #draw the bilding and the num floor
    pygame.draw.rect(screen, (BG), rect_b)
    
    for i in range(NUM_FLOORS):
    
        num  = str(i)
        text = font.render( num, True, my_b.floors[i].col_press, BG) 

        # timer_f = str(int(my_b.floors[i].timer))
        timer_f = my_b.floors[i].timer_print
        timer_floor = font_timer.render(timer_f, True, BG, BLACK)
        screen.blit(text, (20, my_b.floors[i].y_position))
   
        if my_b.floors[i].col_press == GREEN:
           screen.blit(timer_floor, (85, my_b.floors[i].y_position + 10))
    
    #print the elv img 
    for i in range(NUM_ELV):
        screen.blit(my_b.elv[i].img, (my_b.elv[i].x_position,my_b.elv[i].y_position))
        
    #get mouse click, to get req floor or exit 
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # get new request
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] >  15 and pos[0] < 80 and pos[1] > 30:
                for i in range(NUM_FLOORS):
                    # where the clike was(in which floor) : sand the num req floor to my_b
                    if pos[1] > my_b.floors[i].y_position and   pos[1] < (my_b.floors[i].y_position + 50):  
                        my_b.get_request(i)

    my_b.update_all()
    pygame.display.update()

pygame.quit()


#יש עדיין באג : אם מזמינים מעלית לקומה מסויימת בכמה לחיצות אז המעלית תביא מעלית חדשה אע"פ שיש שם כבר מעלית
#הסיבה לכך היא בגלל כאשר אנו מזמינים מעלית אז יש לה 2 שניות המתנה בקומה מה שגורם לקונפליקט שאע"פ שיש מעלית אבל היא לא פנויה כביכול 
#לכן מגיע מעלית אחרת 
#הדרך לפתרון את זה ע"י דגל שמציין שיש שם מעלית 
#צבע שחור לא יכול להיות הדגל כמו שחשבתי מיכוון 
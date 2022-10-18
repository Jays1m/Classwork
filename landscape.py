from ctypes.wintypes import SIZE
from os import system
import pygame, sys
import math
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

# Setup
pygame.init()
clock = pygame.time.Clock()

 #  Variables
circle_x = -30
circle_y = 0
Cycle = 1
cloud_x = 0
cloud_y = 100

# Loop

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

#  Background
    
    WIDTH = 640
    HEIGHT = 480
    SIZE = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode((SIZE))  
      
# Colours

    Light_grey1 = (250, 250, 250)
    Light_grey2 = (105, 105, 105)
    Light_grey3 = (131, 139, 139)
    Grey = (80, 80, 80)
    Dark_grey = (99, 99, 99)
    Cyan = (83, 134, 139)
    Yellow = (227, 207, 87)
    Yellow2 = (255, 215, 0)
    Black = (0, 0, 0)
    Dark_blue = (25,25,112)
    white = (255,255,255)

# Day

    # Sun
    if Cycle == 1:
        screen.fill((151,255,255))
        circle_x += 2
        amplitude = HEIGHT
        y_offset = amplitude / 2 + 30
        circle_y = -1 * (math.sin(circle_x / WIDTH * math.pi) * amplitude / 2) + y_offset

        if circle_x > WIDTH + 30:
            circle_x = -30

        if circle_x >= 669:
            Cycle += 1

    # CLOUDS

        cloud_x += .5
        pygame.draw.ellipse(screen, white, (cloud_x+60, cloud_y-10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+40, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x-40, cloud_y-30, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x, cloud_y-30, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x, cloud_y, 100, 75 ))

        pygame.draw.ellipse(screen, white, (cloud_x+260, cloud_y+30, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+240, cloud_y+50, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+240, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+200, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+200, cloud_y+40, 100, 75 ))

        pygame.draw.ellipse(screen, white, (cloud_x-260, cloud_y+30, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x-240, cloud_y+50, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x-280, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x-200, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x-200, cloud_y+40, 100, 75 ))

        pygame.draw.ellipse(screen, white, (cloud_x+460, cloud_y+30, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+440, cloud_y+50, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+440, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+400, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+400, cloud_y+40, 100, 75 ))

        pygame.draw.ellipse(screen, white, (cloud_x+660, cloud_y+30, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+640, cloud_y+50, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+640, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+600, cloud_y+10, 100, 75 ))
        pygame.draw.ellipse(screen, white, (cloud_x+600, cloud_y+40, 100, 75 ))
        if cloud_x > 650:
            cloud_x = -600


    # CN TOWER
        pygame.draw.rect(screen, Grey, (200, 380, 300, 540)),
        pygame.draw.rect(screen, Black, (200, 380, 300, 540), 3),        
        pygame.draw.circle(screen, Yellow2, (circle_x, circle_y), 30)
        pygame.draw.line(screen, Light_grey3, [280, 40], [280, 440], 60),
        pygame.draw.line(screen, Light_grey3, [280, 0], [280, 440], 30),
        pygame.draw.rect(screen, Light_grey3, (230, 100, 100, 400)),
        pygame.draw.rect(screen, Black, (230, 100, 100, 400), 3),        
        pygame.draw.rect(screen, Cyan, (255, 100, 50, 400)),
        pygame.draw.rect(screen, Black, (255, 100, 50, 400), 3),
        pygame.draw.ellipse(screen, Light_grey3, (180, 70, 200, 150)),
        pygame.draw.rect(screen, Light_grey3, (220, 180, 120, 40)),
        pygame.draw.rect(screen, Cyan, (190, 130, 178, 40)),
        pygame.draw.rect(screen, Black, (190, 130, 178, 40), 3),
        pygame.draw.rect(screen, Light_grey3, (220, 70, 120, 40)),

    # BUILDINGS

        # BUILDING 1
        pygame.draw.rect(screen, Grey, (0, 280, 100, 440)),
        pygame.draw.rect(screen, Black, (0, 280, 100, 440), 3),
        pygame.draw.rect(screen, Light_grey1, (10, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (10, 420, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (60, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (60, 420, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (10, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (10, 360, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (60, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (60, 360, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (10, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (10, 300, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (60, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (60, 300, 25, 40), 3),

        # BUILDING 2
        pygame.draw.rect(screen, Dark_grey, (100, 340, 100, 440)),
        pygame.draw.rect(screen, Black, (100, 340, 100, 440), 3),
        pygame.draw.rect(screen, Light_grey1, (160, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (160, 420, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (120, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (120, 420, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (160, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (160, 360, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (120, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (120, 360, 25, 40), 3),

        # BUILDING 3
        pygame.draw.rect(screen, Grey, (540, 280, 100, 440)),
        pygame.draw.rect(screen, Black, (540, 280, 100, 440),3)    
        pygame.draw.rect(screen, Light_grey1, (560, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (560, 420, 25, 40),3)
        pygame.draw.rect(screen, Light_grey1, (600, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (600, 420, 25, 40),3)
        pygame.draw.rect(screen, Light_grey1, (560, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (560, 360, 25, 40),3)
        pygame.draw.rect(screen, Light_grey1, (600, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (600, 360, 25, 40),3)
        pygame.draw.rect(screen, Light_grey1, (560, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (560, 300, 25, 40),3)
        pygame.draw.rect(screen, Light_grey1, (600, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (600, 300, 25, 40),3),

        # BUILDING 4
        pygame.draw.rect(screen, Dark_grey, (440, 340, 100, 440)),
        pygame.draw.rect(screen, Black, (440, 340, 100, 440), 3),
        pygame.draw.rect(screen, Light_grey1, (460, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (460, 420, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (500, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (500, 420, 25, 40),3),
        pygame.draw.rect(screen, Light_grey1, (460, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (460, 360, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (500, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (500, 360, 25, 40), 3),

         # BUILDING 5
        pygame.draw.rect(screen, Grey, (340, 280, 100, 440)),
        pygame.draw.rect(screen, Black, (340, 280, 100, 440), 3),
        pygame.draw.rect(screen, Light_grey1, (360, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (360, 420, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (400, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (400, 420, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (360, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (360, 360, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (400, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (400, 360, 25, 40), 3),
        pygame.draw.rect(screen, Light_grey1, (360, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (360, 300, 25, 40),3),    
        pygame.draw.rect(screen, Light_grey1, (400, 300, 25, 40))
        pygame.draw.rect(screen, Black, (400, 300, 25, 40),3),    


#  Night

    # MOON
    if Cycle == 2:
        screen.fill((Dark_blue))
        circle_x += 3
        amplitude = HEIGHT
        y_offset = amplitude / 2 + 30
        circle_y = -1 * (math.sin(circle_x / WIDTH * math.pi) * amplitude / 2) + y_offset

        if circle_x > WIDTH + 30:
            circle_x = -30

        if circle_x >= 669:
            Cycle -= 1
        




        # CN TOWER
        pygame.draw.rect(screen, Grey, (200, 380, 300, 540)),
        pygame.draw.rect(screen, Black, (200, 380, 300, 540), 3),        
        pygame.draw.circle(screen, (Light_grey1), (circle_x, circle_y), 30)
        pygame.draw.line(screen, Light_grey3, [280, 40], [280, 440], 60),
        pygame.draw.line(screen, Light_grey3, [280, 0], [280, 440], 30),
        pygame.draw.rect(screen, Light_grey3, (230, 100, 100, 400)),
        pygame.draw.rect(screen, Black, (230, 100, 100, 400), 3),        
        pygame.draw.rect(screen, Yellow, (255, 100, 50, 400)),
        pygame.draw.rect(screen, Black, (255, 100, 50, 400), 3),
        pygame.draw.ellipse(screen, Light_grey3, (180, 70, 200, 150)),
        pygame.draw.rect(screen, Light_grey3, (220, 180, 120, 40)),
        pygame.draw.rect(screen, Yellow, (190, 130, 178, 40)),
        pygame.draw.rect(screen, Black, (190, 130, 178, 40), 3),
        pygame.draw.rect(screen, Light_grey3, (220, 70, 120, 40)),

    # STARS

        if circle_x >= 30:
            pygame.draw.circle(screen, Light_grey1, (100, 200), 2)
            pygame.draw.circle(screen, Light_grey1, (50, 150), 2)
            pygame.draw.circle(screen, Light_grey1, (40, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (160, 300), 2)
            pygame.draw.circle(screen, Light_grey1, (100, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (50, 250), 2)
            pygame.draw.circle(screen, Light_grey1, (40, 200), 2)
            pygame.draw.circle(screen, Light_grey1, (160, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (100, 10), 2)
            pygame.draw.circle(screen, Light_grey1, (50, 90), 2)
            pygame.draw.circle(screen, Light_grey1, (40, 40), 2)
            pygame.draw.circle(screen, Light_grey1, (160, 30), 2)

            pygame.draw.circle(screen, Light_grey1, (400, 200), 2)
            pygame.draw.circle(screen, Light_grey1, (500, 150), 2)
            pygame.draw.circle(screen, Light_grey1, (400, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (460, 300), 2)
            pygame.draw.circle(screen, Light_grey1, (400, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (506, 250), 2)
            pygame.draw.circle(screen, Light_grey1, (404, 200), 2)
            pygame.draw.circle(screen, Light_grey1, (562, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (420, 10), 2)
            pygame.draw.circle(screen, Light_grey1, (540, 90), 2)
            pygame.draw.circle(screen, Light_grey1, (320, 40), 2)
            pygame.draw.circle(screen, Light_grey1, (540, 30), 2)
            pygame.draw.circle(screen, Light_grey1, (560, 150), 2)
            pygame.draw.circle(screen, Light_grey1, (640, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (540, 300), 2)
            pygame.draw.circle(screen, Light_grey1, (630, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (624, 250), 2)
            pygame.draw.circle(screen, Light_grey1, (615, 200), 2)
            pygame.draw.circle(screen, Light_grey1, (514, 100), 2)
            pygame.draw.circle(screen, Light_grey1, (100, 10), 2)

        # BUILDINGS

            # BUILDING 1
        pygame.draw.rect(screen, Grey, (0, 280, 100, 440)),
        pygame.draw.rect(screen, Black, (0, 280, 100, 440), 3),
        pygame.draw.rect(screen, Yellow, (10, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (10, 420, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (60, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (60, 420, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (10, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (10, 360, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (60, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (60, 360, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (10, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (10, 300, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (60, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (60, 300, 25, 40), 3),

        # BUILDING 2
        pygame.draw.rect(screen, Dark_grey, (100, 340, 100, 440)),
        pygame.draw.rect(screen, Black, (100, 340, 100, 440), 3),
        pygame.draw.rect(screen, Yellow, (160, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (160, 420, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (120, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (120, 420, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (160, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (160, 360, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (120, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (120, 360, 25, 40), 3),

        # BUILDING 3
        pygame.draw.rect(screen, Grey, (540, 280, 100, 440)),
        pygame.draw.rect(screen, Black, (540, 280, 100, 440),3)    
        pygame.draw.rect(screen, Yellow, (560, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (560, 420, 25, 40),3)
        pygame.draw.rect(screen, Yellow, (600, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (600, 420, 25, 40),3)
        pygame.draw.rect(screen, Yellow, (560, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (560, 360, 25, 40),3)
        pygame.draw.rect(screen, Yellow, (600, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (600, 360, 25, 40),3)
        pygame.draw.rect(screen, Yellow, (560, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (560, 300, 25, 40),3)
        pygame.draw.rect(screen, Yellow, (600, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (600, 300, 25, 40),3),

        # BUILDING 4
        pygame.draw.rect(screen, Dark_grey, (440, 340, 100, 440)),
        pygame.draw.rect(screen, Black, (440, 340, 100, 440), 3),
        pygame.draw.rect(screen, Yellow, (460, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (460, 420, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (500, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (500, 420, 25, 40),3),
        pygame.draw.rect(screen, Yellow, (460, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (460, 360, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (500, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (500, 360, 25, 40), 3),

         # BUILDING 5
        pygame.draw.rect(screen, Grey, (340, 280, 100, 440)),
        pygame.draw.rect(screen, Black, (340, 280, 100, 440), 3),
        pygame.draw.rect(screen, Yellow, (360, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (360, 420, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (400, 420, 25, 40)),
        pygame.draw.rect(screen, Black, (400, 420, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (360, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (360, 360, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (400, 360, 25, 40)),
        pygame.draw.rect(screen, Black, (400, 360, 25, 40), 3),
        pygame.draw.rect(screen, Yellow, (360, 300, 25, 40)),
        pygame.draw.rect(screen, Black, (360, 300, 25, 40),3),    
        pygame.draw.rect(screen, Yellow, (400, 300, 25, 40))
        pygame.draw.rect(screen, Black, (400, 300, 25, 40),3),   



    pygame.display.flip()
    pygame.display.update()
    FPS = clock.tick(60)

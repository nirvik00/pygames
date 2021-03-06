import pygame
import time
import random

pygame.init()


display_width=800
display_height=600

black=(0,0,0)
red=(255,0,0)
white=(255,255,255)

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game-1')
clock=pygame.time.Clock()

carImg=pygame.image.load('racecar.jpg')

def thing(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center=(display_width/2,display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text,font):
    textSurface=font.render(text,True, black)
    return textSurface, textSurface.get_rect()

def crash():
    message_display('You Crashed')


def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def game_loop():
    x=display_width*0.45
    y=display_height*0.85
    x_change=0

    thing_startx=random.randrange(0,display_width)
    thing_starty=random.randrange(0,display_height)
    thing_speed=15
    thing_width=10
    thing_height=100

    thingCount=1
    dodged=0
    
    gameExit=False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-15
                elif event.key == pygame.K_RIGHT:
                    x_change=15
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
            x+=x_change                
        gameDisplay.fill(white)


        car(x,y)
        things_dodged(dodged)
        
        if x>display_width or x<0:            
            crash()

        if(y>thing_starty and y<thing_starty+thing_height):
            print('y crossover')
            if(x>thing_startx and x<thing_startx+thing_width):
                print('x crossover')
                crash()
            
                
        thing(thing_startx,thing_starty,thing_width,thing_height,red)
        thing_starty+=thing_speed
        if(thing_starty>display_height):
            thing_starty=0
            thing_startx=random.randrange(0,display_width)
            dodged+=1
            if(thing_startx>display_width):
                thing_startx=0
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

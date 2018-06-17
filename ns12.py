import pygame
import random
import time

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

display_height=600
display_width=800

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game-2')
gameDisplay.fill(black)


def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=(display_width/2,display_height/2)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface, textSurface.get_rect()



def game_loop():
    gameExit=False
    while not gameExit:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        print('in game')

game_loop()
pygame.quit()
quit()



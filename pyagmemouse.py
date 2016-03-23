import pygame, random
import pyautogui

def printme( mes,posX,posY ):
   "This prints a passed string into this function"
   print mes,"  ",posX,"  ",posY
   return

screenWidth, screenHeight = pyautogui.size()  
pyautogui.moveTo(screenWidth/2, screenHeight/2)
title = "Hello!"
pygame.init()
screen = pygame.display.set_mode((screenWidth/2, screenHeight/2))#,pygame.FULLSCREEN)
running = True
clock = pygame.time.Clock()
pygame.display.set_caption(title)
even = "null"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            even = "move"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (l,m,r) = pygame.mouse.get_pressed()
            if(l):
                even = "left"
            elif(r):
                even = "right"
            else:
                even = "scroll"
        (posX,posY) = pyautogui.position()
        printme(even,posX,posY)
    clock.tick(240)
pygame.quit()
#pygame.mouse.get_pressed()
#click = pygame.mouse.get_pressed()
    #print(click)



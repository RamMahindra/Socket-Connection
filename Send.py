import socket   #for sockets
import sys  #for exit
import pygame, random
import pyautogui


def printme( mes,posX,posY ):                                                           ##function 
   "This prints a passed string into this function"
   print mes,"  ",posX,"  ",posY
   return

screenWidth, screenHeight = pyautogui.size()                                            ##pygame
pyautogui.moveTo(screenWidth/2, screenHeight/2)
title = "Hello!"
pygame.init()
screen = pygame.display.set_mode((screenWidth/2, screenHeight/2))#,pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption(title)
even = "null"
running = True


 
try:                                                                                    ##socket creation
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
print 'Socket Created'
 
#host = '172.20.24.244' #this system
host = socket.gethostname()
port = 1234
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
 
#Connect to remote server
s.connect((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip
 
###Send some data to remote server
##message = "You are working"
## 
##try :
##    #Set the whole string
##    s.sendall(message)
##except socket.error:
##    #Send failed
##    print 'Send failed'
##    sys.exit()
## 
##print 'Message send successfully'

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
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_a:
                even = "a"
             elif  event.key == pygame.K_d:
                even = "b"
             elif event.key == pygame.K_w:
                even = "w"
             elif event.key == pygame.K_s:
                even = "s"
             else:
                even = "other"
        (posX,posY) = pyautogui.position()
        m = even+" "+str(posX)+" "+str(posY)
        s.send(m)
    clock.tick(240)
##    msg = raw_input('CLIENT >> ')
##    s.send(msg)
##    msg = s.recv(1024)
##    print 'SERVER >> ', msg
s.close                     # Close the socket when done

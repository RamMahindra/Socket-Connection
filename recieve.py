#Socket client example in python
 
import socket   #for sockets
import sys  #for exit
import pyautogui
 
#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
     
print 'Socket Created'
 
#host = 'www.google.com';
#port = 80;
#host = '172.20.24.244'
host = socket.gethostname()
port = 1234
 
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
 
#Connect to remote server
s.bind((remote_ip , port))
 
print 'Socket Connected to ' + host + ' on ip ' + remote_ip


s.listen(5)                 # Now wait for client connection. 
#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
   
 
#try :
#   #Set the whole string
#    s.sendall(message)
#except socket.error:
#    #Send failed
#    print 'Send failed'
#    sys.exit()
 
#print 'Message send successfully'
 
#Now receive data
while True:
    msg = c.recv(1024)
    z1 = msg.split('.')
    if (z1[0] == "move"):
        pyautogui.moveRel(int(z1[1]),int(z1[2]))
    elif (z1[0] == "left"):
        pyautogui.click()
    elif (z1[0] == "w"):
        pyautogui.typewrite(['w'])
    elif (z1[0] == "b"):
        pyautogui.typewrite(['b'])
    elif (z1[0] == "a"):
        pyautogui.typewrite(['a'])
#c.close()   

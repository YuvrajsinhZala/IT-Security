#Control Mouse

from pynput.mouse import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (1520, 10)
    #1520 is for left to right & 10 is for top to bottom
    #Top left ni screen 0,0 ni hoy

controlMouse()

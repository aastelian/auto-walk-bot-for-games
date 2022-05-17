import keyboard
import pyautogui as pag


class scumBot:

    def autoWalk(self):
            
            keyboard.wait("ctrl+w")
            #keyboard.wait("w")
            
            while True:
                
                pag.keyDown("w")
                if keyboard.is_pressed("s"):
                    pag.keyUp("w")
                    break

while True:
    scumBot().autoWalk()


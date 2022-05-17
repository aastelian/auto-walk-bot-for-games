import keyboard,time
import pyautogui as pag


class scumBot:

    def autoWalk(self):
            
            keyboard.wait("ctrl+w")
            #keyboard.wait("w")
            stop = 0
            while True:
                if stop ==0 :
                    pag.keyDown("w")
                if keyboard.is_pressed("s"):
                    pag.keyUp("w")
                    break
time.sleep(5)
while True:
    scumBot().autoWalk()


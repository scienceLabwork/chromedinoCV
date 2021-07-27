"""
    DEVELOPED BY RUDRA SHAH UNDER THE PEN NAME OF SCIENCELABWORK
"""
import time
from colorthief import ColorThief
import cv2
import mss
import numpy 
from PIL import Image
import pyautogui
import os
import shutil
from rgbconverter import rgb2hex

chromedinotext = """
  ____ _                              ____  _             
 / ___| |__  _ __ ___  _ __ ___   ___|  _ \(_)_ __   ___  
| |   | '_ \| '__/ _ \| '_ ` _ \ / _ \ | | | | '_ \ / _ \ 
| |___| | | | | | (_) | | | | | |  __/ |_| | | | | | (_) |
 \____|_| |_|_|  \___/|_| |_| |_|\___|____/|_|_| |_|\___/ 

"""
print(chromedinotext)

# Frame Counter
c = 0

print("\n Please Change the value of TOP and LEFT variable on line 32 and 33 respectively. IF YOU FIND THAT IT IS NOT WORKING THEN ONLY CHANGE THE VALUE")

# NOTE: IF YOU FIND THAT IT IS NOT WORKING THEN ONLY CHANGE THE VALUE
# Change value to fine tune the dino
top = 398
left = 240

with mss.mss() as sct:
    print("\n Switch to Chrome Screen \n")
    time.sleep(1.4)
    while "Screen capturing":
        c+=1
        # Part of the screen to capture
        monitor = {"top": top, "left": left+(c/10), "width": 10+(c/10), "height": 109}
        last_time = time.time()
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture to conputer
        cv2.imwrite("frames/image"+str(c)+".png", img)

        # Getting Colors
        img = Image.open("frames/image"+str(c)+".png")
        colors = img.convert('RGB').getcolors()

        #Making a array of colors available
        l = []
        if(not None):
            try:
                for i in colors:
                    m = list(list(i)[1])
                    l.append(rgb2hex(m[0],m[1],m[2]))
            except:
                print("\n Restart the game and Please switch to Chrome Screen when commanded.")
                break

        #Checking if color exisit in capture window or not
        if("#535353" in l or "#545454" in l or "#acacac" in l or "#ffd200" in l or "#d43100" in l):
            print("Jump at frame", c)
            pyautogui.press("up")

        #Deleting frame/second
        os.remove("frames/image"+str(c)+".png")
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
shutil.rmtree("frames")
os.mkdir("frames")
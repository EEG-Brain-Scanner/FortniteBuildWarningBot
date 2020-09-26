import math
import time
from PIL import ImageGrab
import pytesseract
import winsound
import os

#---------------USER-CUSTOMIZABLE-SETTINGS---------------#
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Evan\AppData\Local\Tesseract-OCR\tesseract.exe'
    #path of tesseract.exe (should just have to change USERSNAME if installed in default location

ExecutableCodeFileLocation = r'C:\Users\Evan\Desktop\Fortnite Build Warning Bot'
    #Location of 'Executable Code'
    #Can be found by right click on 'Executable Code' file > Properties > Then highlight and copy Location
    #YOU MUST LEAVE 'Executable Code' file in the folder with the 3 sound files
    #You can rename the folder if desired

RES = (2560, 1440) #must be 16:9
    #resolution of your monitor
#--------------------------------------------------------#

running = ''
winsound.Beep(300, 300)

CommonZero = ['QO', 'Q0', 'Oo', '0o', 'Q', 'O', 'o', '0']
Wood, Brick, Metal, Builds = 0, 0, 0, 0
Ready20, Ready10, Ready5 = False, False, False

HorizontalConst = ((2310/2560), (2880/2880)) #factors found in photoshopr
VerticalConst = ((1020/1440), (1060/1440))

X1 = math.floor(RES[0] * HorizontalConst[0]) #round down to make sure nothing is cut off
X2 = math.floor(RES[0] * HorizontalConst[1]) #round down to make sure not outside of the screen
Y1 = math.floor(RES[1] * VerticalConst[0])
Y2 = math.floor(RES[1] * VerticalConst[1])

while True:
    time.sleep(0.5)
    
    screenshot = ImageGrab.grab(bbox=(X1, Y1, X2, Y2))
    screenshot = screenshot.point(lambda x: 255 if x<255 else 0)
    #screenshot.show()

    Materials = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 7')

    if len(Materials.split()) == 3: #just ignore if we do not find 3 strings
        Materials = Materials.split()

        if Materials[0].isdigit() == True:
            Wood = int(Materials[0])
        elif Materials[0] in CommonZero:
            Wood = 0
            
        if Materials[1].isdigit() == True:
            Brick = int(Materials[1])
        elif Materials[1] in CommonZero:
            Brick = 0

        if Materials[2].isdigit() == True:
            Metal = int(Materials[2])
        elif Materials[2] in CommonZero:
            Metal = 0

        Builds = math.floor(Wood/10) + math.floor(Brick/10) + math.floor(Metal/10)

    if Builds < 20 and Ready20 == True:
        winsound.PlaySound(ExecutableCodeFileLocation + r'\20builds.wav', winsound.SND_ASYNC)
        Ready20 = False
    elif Builds < 10 and Ready10 == True:
        winsound.PlaySound(ExecutableCodeFileLocation + r'\10builds.wav', winsound.SND_ASYNC)
        Ready10 = False
    elif Builds < 5 and Ready5 == True:
        winsound.PlaySound(ExecutableCodeFileLocation + r'\5builds.wav', winsound.SND_ASYNC)
        Ready5 = False
        
    if Builds > 30:
        Ready20, Ready10, Ready5 = True, True, True

    if len(running) == 3:
        running = "."
    else:
        running = running + '.'
    os.system('cls')
    print("Bot is running" + running)
    print("Current Builds: " + str(Builds))
        

from operator import truediv
import sys
from turtle import window_height
import pyautogui as pg
import multiprocessing as mp
import time
import keyboard
import ctypes
import os
import win32gui
import win32api 

MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
# whack time (edit)
gameTimer = 60
# keep track of pause state
paused = True 
# keep track of playing once state
playOnce = False
# calibration process
calibrationProcess = None
# multi process manager 
manager = None

def launchAutoclicker():
    counterGreen=0
    appearenceX=-1
    appearenceY=-1
    autoCalibration()
    comboSaves=getComboSaves()
    while True:
        # Get toilets screenshot and check for potatoes
        screenshot = pg.screenshot(region=(sceneScreenshotCornerX, sceneScreenshotCornerY, sceneScreenshotWidth, sceneScreenshotHeight))
        for y in range(topBorderToToilet, sceneScreenshotHeight, toiletToToiletY): # 3 rows
            for x in range(leftBorderToToilet, sceneScreenshotWidth, toiletToToiletX): # 5 columns
                r,g,b = screenshot.getpixel((x,y))
                if (r in range(70,120) and g in range(170,230) and b in range(0,25)) or (r in range(210,255) and g in range(160,220) and b in range(0,25)):
                    if appearenceX == x and appearenceY == y:
                        continue
                    appearenceX = x
                    appearenceY = y
                    pg.click(x + sceneScreenshotCornerX + toToiletMiddle,y + sceneScreenshotCornerY)
                elif r in range(200,230) and g in range(20,60) and b in range(0,25) : # if green
                    if appearenceX == x and appearenceY == y:
                        continue
                    appearenceX = x
                    appearenceY = y
                    if counterGreen < comboSaves:
                        pg.click(x + sceneScreenshotCornerX + toToiletMiddle,y + sceneScreenshotCornerY)
                        counterGreen+=1
def getComboSaves():
    comboSavesCounter=0
    screenshot = pg.screenshot(region=(comboX, comboY, comboScreenshotWidth, comboScreenshotHeight))
    for y in range(comboMiddleY,comboScreenshotHeight,comboToComboY):
        r,g,b = screenshot.getpixel((comboMiddleX,y))
        if r in range(140,152) and g in range(140,152) and b in range(140,152):
            comboSavesCounter+=1
    return comboSavesCounter


def autoCalibration():
    if sys.platform == "win32":
        def callback(hwnd, extra):
            rect = win32gui.GetWindowRect(hwnd)

            if win32gui.GetWindowText(hwnd) == "Farmer Against Potatoes Idle":
                windowX = rect[0] + 9
                windowY = rect[1] + 35
                windowWidth = rect[2] - windowX
                windowHeight = rect[3] - windowY
                calculatePositions(windowX,windowY,windowWidth,windowHeight)
        win32gui.EnumWindows(callback, None)
    elif sys.platform == "linux" or sys.platform == "linux2":
        #linux
        print("linux not supported")
        os._exit(0)
    elif sys.platform == "darwin":
        #ios
        print("ios not supported")
        os._exit(0)
def calculatePositions(uncorrectedWindowX,uncorrectedWindowY, uncorrectedWindowWidth,uncorrectedWindowHeight):
        global sceneScreenshotCornerX, sceneScreenshotCornerY, sceneScreenshotWidth, sceneScreenshotHeight, leftBorderToToilet
        global topBorderToToilet, toToiletMiddle, toiletToToiletX, toiletToToiletY, startButtonX, startButtonY, startScreenshotCornerX, startScreenshotCornerY
        global  comboX, comboY, comboMiddleX,comboMiddleY, comboToComboY, comboScreenshotHeight,comboScreenshotWidth

        windowX = uncorrectedWindowX
        windowY = uncorrectedWindowY
        windowWidth = uncorrectedWindowWidth
        windowHeight = uncorrectedWindowHeight

        windowDelta= (windowWidth/windowHeight) / (1785/1000)
    
        if windowDelta > 1:
            windowX = int(windowX + (windowWidth - int(windowWidth / windowDelta))/(2000/1000)+4)
            windowWidth= int(windowWidth / windowDelta)
        else:
            windowY = int(windowY + (windowHeight - int(windowHeight * windowDelta))/(2000/1000))
            windowX +=2
            windowHeight= int(windowHeight * windowDelta)

        sceneScreenshotCornerY =int(windowHeight /100 * 17.9)+windowY
        testBottomY=int(windowHeight/100 * 80.5)+windowY
        sceneScreenshotCornerX = int(windowWidth / 100 * 15.6)+windowX
        testRightX = int(windowWidth / 100 * 51.8)+windowX
        sceneScreenshotWidth=testRightX-sceneScreenshotCornerX
        sceneScreenshotHeight=testBottomY -sceneScreenshotCornerY
        toToiletMiddle = int(windowWidth / 100 * 3.24)
        topBorderToToilet = int(windowHeight / 100 * 13.2)
        leftBorderToToilet = int(windowWidth / 100 * 0.55)
        toiletToToiletX = int(windowWidth / 100 * 7.25)
        toiletToToiletY = int(windowHeight / 100 * 21.3)
        startButtonX = int(windowWidth / 100 * 34) + windowX
        startButtonY = int(windowHeight / 100 * 95) + windowY
        startScreenshotCornerX = int(windowWidth / 100 * 20) + windowX
        startScreenshotCornerY = int(windowHeight / 100 * 6.5) + windowY

        comboX=int(windowWidth / 100 * 53.4) + windowX
        rightComboX=int(windowWidth / 100 * 59.25) + windowX
        comboY=int(windowHeight / 100 * 29) + windowY
        bottomComboY=int(windowHeight / 100 * 70.6) + windowY
        comboMiddleY = int(windowHeight / 100 * 3.2)
        comboMiddleX = int (windowHeight / 100 * 3)
        comboToComboY =  int(windowHeight / 100 * 7.75)
        comboScreenshotWidth = rightComboX -comboX
        comboScreenshotHeight = bottomComboY - comboY

def showCalibration():
    initPainters()
    while True:
        autoCalibration()
        paintQuadre(sceneScreenshotCornerX,sceneScreenshotCornerY,0,255,0)
        paintQuadre(sceneScreenshotCornerX+sceneScreenshotWidth,sceneScreenshotCornerY,0,255,0)
        paintQuadre(sceneScreenshotCornerX,sceneScreenshotCornerY+sceneScreenshotHeight,0,255,0)
        paintQuadre(sceneScreenshotCornerX+sceneScreenshotWidth,sceneScreenshotCornerY+sceneScreenshotHeight,0,255,0)
        paintQuadre(startButtonX,startButtonY,0,255,0)
        for y in range(topBorderToToilet, sceneScreenshotHeight, toiletToToiletY): # 3 rows
            for x in range(leftBorderToToilet, sceneScreenshotWidth, toiletToToiletX):
                paintQuadre(x+sceneScreenshotCornerX,y+sceneScreenshotCornerY,0,255,0)
                paintQuadre(x+sceneScreenshotCornerX+toToiletMiddle,y+sceneScreenshotCornerY,0,255,0)
        for x in range(0, 10):
            paintQuadre(x+startScreenshotCornerX,startScreenshotCornerY,0,255,0)
        
        paintQuadre(comboX,comboY,0,255,0)
        paintQuadre(comboX+comboScreenshotWidth,comboY,0,255,0)
        paintQuadre(comboX,comboY+comboScreenshotHeight,0,255,0)
        paintQuadre(comboX+comboScreenshotWidth,comboY+comboScreenshotHeight,0,255,0)

        for y in range(comboMiddleY,comboScreenshotHeight,comboToComboY):
            paintQuadre(comboX+comboMiddleX,y+comboY,0,255,0)

def initPainters():
    global dc
    if sys.platform == "win32":
        dc = win32gui.GetDC(0)
    elif sys.platform == "linux" or sys.platform == "linux2":
        #linux
        print("linux not supported")
        os._exit(0)
    elif sys.platform == "darwin":
        #ios
        print("ios not supported")
        os._exit(0)
def paintQuadre(x,y,r,g,b, size = 1):
    for i in range(-size,size):
        for j in range(-size,size):
            if sys.platform == "win32":
                win32gui.SetPixel(dc, x+i, y+j, win32api.RGB(r, g, b))  # draw red at x,y
            elif sys.platform == "linux" or sys.platform == "linux2":
                #linux
                print("linux not supported")
                os._exit(0)
            elif sys.platform == "darwin":
                #ios
                print("ios not supported")
                os._exit(0)

def main():
    global paused, playOnce, manager
    clickerProcess = None 
    keySetup()
    while True:
        if clickerProcess != None and clickerProcess.is_alive():
            clickerProcess.kill()
            print('[internal] killed sub process')
        if not isStartable():
            time.sleep(1)
            continue
        if (playOnce or not paused):
            clickerProcess = mp.Process(target=launchAutoclicker,args=())
            clickerProcess.start()
            pg.click(startButtonX, startButtonY)
            playOnce = False
            time.sleep(gameTimer + 5)
        time.sleep(1);
def isStartable():
    autoCalibration()
    screenshot = pg.screenshot(region=(startScreenshotCornerX, startScreenshotCornerY, 50, 1))
    for startX in range(0, 10):
        r,g,b =screenshot.getpixel((startX, 0))
        if r in range(0,10) and g in range(0,10) and b in range(0,10):
            if checkIfWhackPageOpenAndNotPlaying():
                print("[internal] start is available")
                return True
    return False

def checkIfWhackPageOpenAndNotPlaying():
    screenshot = pg.screenshot(region=(sceneScreenshotCornerX, sceneScreenshotCornerY, sceneScreenshotWidth, sceneScreenshotHeight))
    for y in range(topBorderToToilet, sceneScreenshotHeight, toiletToToiletY): 
        for x in range(leftBorderToToilet, sceneScreenshotWidth, toiletToToiletX):
            r,g,b = screenshot.getpixel((x,y))
            if not (r in range(160,230) and g in range(85,130) and b in range(15,45)):
                return False
            r,g,b = screenshot.getpixel((x+toToiletMiddle,y))
            if not (r in range(0,10) and g in range(0,10) and b in range(0,10)):
                return False
    return True

def keySetup():
    print("Press 'f10' when you wanna idle - You can pause with'f10' at anytime (the running game is not affected and will complete first)")
    print("Press 'f9' when you wanna play one game")
    print("Press 'f8' shows the calibration - be aware if you activate this while whacking, the auto whacking will stop")
    print("Press 'f7' when you wanna terminate the script")
    def callbackF10(event):
        global paused
        paused = not paused
        if paused:
            print('You paused auto whack')
            time.sleep(0.1)
        else:
            print('You unpaused auto whack')
            killCalibrationProcess()
            time.sleep(0.1)
    def callbackF9(event):
        global playOnce
        playOnce = not playOnce
        if playOnce:
            print('Play once is on')
            killCalibrationProcess()
            time.sleep(0.1)
        else:
            print('Play once is off')
            time.sleep(0.1)
    def callbackF8(event):
        global calibrationProcess,manager
        if calibrationProcess == None:
            print('Show claibration')
            calibrationProcess = mp.Process(target=showCalibration)
            calibrationProcess.start()
        else:
            killCalibrationProcess()

    def callbackF7(event):
         os._exit(0)
    # if key 'f10' is pressed -> pause / unpause
    keyboard.on_press_key("f10", callbackF10)
    # if key 'f9' is pressed -> playOnce
    keyboard.on_press_key("f9", callbackF9)
    # if key 'f8' is pressed -> calibration
    keyboard.on_press_key("f8", callbackF8)
    # if key 'f7' is pressed -> terminate
    keyboard.on_press_key("f7", callbackF7)

def killCalibrationProcess():
    global calibrationProcess
    if(calibrationProcess != None):
        print('Hide calibration')
        calibrationProcess.kill()
        calibrationProcess = None;

def clickAtPos(x,y):
    if sys.platform == "win32":
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    elif sys.platform == "linux" or sys.platform == "linux2":
        #linux
        print("linux not supported")
        os._exit(0)
    elif sys.platform == "darwin":
        #ios
        print("ios not supported")
        os._exit(0)
### START ###
if __name__ == '__main__':
    main()
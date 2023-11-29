import sys
import pyautogui as pg
import multiprocessing as mp
import time
import keyboard
import os
import win32gui
import win32api 

MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
# keep track of pause state
paused = True 
# keep track of playing once state
playOnce = False

calibrationProcess = None
clickerProcess = None 
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
                windowY = rect[1] + 34
                windowWidth = rect[2] - windowX - 8
                windowHeight = rect[3] - windowY - 8
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
        global windowX, windowY, windowWidth, windowHeight
        global comboLabelX, comboLabelY
        try:
            screenshot = pg.screenshot(region=(uncorrectedWindowX, uncorrectedWindowY, uncorrectedWindowWidth, uncorrectedWindowHeight))
            screenshot.save("test.jpg")
            for i in range(4, uncorrectedWindowWidth):
                r,g,b = screenshot.getpixel((i, int(uncorrectedWindowHeight/2)))
                if r != 0 and g != 0 and b!=0:
                    windowX=uncorrectedWindowX+i
                    break;
            
            for i in range(uncorrectedWindowWidth-1, windowX,-1):
                r,g,b = screenshot.getpixel((i, int(uncorrectedWindowHeight/2)))
                if r != 0 and g != 0 and b!=0:
                    tmpWindowRightX = i+uncorrectedWindowX
                    break;
            windowWidth=tmpWindowRightX - windowX
            for i in range(0, uncorrectedWindowHeight):
                r,g,b = screenshot.getpixel((int(windowWidth/2), i))
                if r != 0 and g != 0 and b!=0:
                    windowY = i+uncorrectedWindowY
                    break;
            for i in range(uncorrectedWindowHeight-1, windowY,-1):
                r,g,b = screenshot.getpixel((int(windowWidth/2), i))
                if r != 0 and g != 0 and b!=0:
                    tmpWindowBottomY = i+uncorrectedWindowY
                    break;
            windowHeight=tmpWindowBottomY - windowY
            sceneScreenshotCornerY =int(windowHeight /100 * 18.2)+windowY
            testBottomY=int(windowHeight/100 * 81.5)+windowY
            sceneScreenshotCornerX = int(windowWidth / 100 * 15.75)+windowX
            testRightX = int(windowWidth / 100 * 52.25)+windowX
            sceneScreenshotWidth=testRightX-sceneScreenshotCornerX
            sceneScreenshotHeight=testBottomY -sceneScreenshotCornerY
            toToiletMiddle = int(windowWidth / 100 * 3.15)
            topBorderToToilet = int(windowHeight / 100 * 13.3)
            leftBorderToToilet = int(windowWidth / 100 * 0.5)
            toiletToToiletX = int(windowWidth / 100 * 7.371)
            toiletToToiletY = int(windowHeight / 100 * 21.6)
            startButtonX = int(windowWidth / 100 * 34) + windowX
            startButtonY = int(windowHeight / 100 * 95) + windowY
            startScreenshotCornerX = int(windowWidth / 100 * 20) + windowX
            startScreenshotCornerY = int(windowHeight / 100 * 6.7) + windowY

            comboX=int(windowWidth / 100 * 53.9) + windowX
            rightComboX=int(windowWidth / 100 * 59.85) + windowX
            comboY=int(windowHeight / 100 * 29.15) + windowY
            bottomComboY=int(windowHeight / 100 * 71.5) + windowY
            comboMiddleY = int(windowHeight / 100 * 3.2)
            comboMiddleX = int (windowHeight / 100 * 3)
            comboToComboY =  int(windowHeight / 100 * 8)
            comboScreenshotWidth = rightComboX -comboX
            comboScreenshotHeight = bottomComboY - comboY

            comboLabelX = int(windowWidth / 100 * 7.5)
            comboLabelY = int(windowHeight / 100 * 6.5) + windowY
        except:
            pass

def showCalibration():
    try:
        initPainters()
        while True:
            autoCalibration()
            paintPixel(windowX,windowY,255,0,0)
            paintPixel(windowX+windowWidth,windowY,255,0,0)
            paintPixel(windowX,windowY+windowHeight,255,0,0)
            paintPixel(windowX+windowWidth,windowY+windowHeight,255,0,0)
            paintPixel(sceneScreenshotCornerX,sceneScreenshotCornerY,0,255,0)
            paintPixel(sceneScreenshotCornerX+sceneScreenshotWidth,sceneScreenshotCornerY,0,255,0)
            paintPixel(sceneScreenshotCornerX,sceneScreenshotCornerY+sceneScreenshotHeight,0,255,0)
            paintPixel(sceneScreenshotCornerX+toToiletMiddle+leftBorderToToilet,sceneScreenshotCornerY+sceneScreenshotHeight,0,255,0)
            paintPixel(sceneScreenshotCornerX+sceneScreenshotWidth,sceneScreenshotCornerY+sceneScreenshotHeight,0,255,0)
            paintPixel(startButtonX,startButtonY,0,255,0)
            for y in range(topBorderToToilet, sceneScreenshotHeight, toiletToToiletY): # 3 rows
                for x in range(leftBorderToToilet, sceneScreenshotWidth, toiletToToiletX):
                    paintPixel(x+sceneScreenshotCornerX,y+sceneScreenshotCornerY,0,255,0)
                    paintPixel(x+sceneScreenshotCornerX+toToiletMiddle,y+sceneScreenshotCornerY,0,255,0)
            for x in range(0, 10):
                paintPixel(x+startScreenshotCornerX,startScreenshotCornerY,0,255,0)
            for x in range(0, 10):
                paintPixel(x+comboLabelX,comboLabelY,0,255,0)
            paintPixel(comboX,comboY,0,255,0)
            paintPixel(comboX+comboScreenshotWidth,comboY,0,255,0)
            paintPixel(comboX,comboY+comboScreenshotHeight,0,255,0)
            paintPixel(comboX+comboScreenshotWidth,comboY+comboScreenshotHeight,0,255,0)

            for y in range(comboMiddleY,comboScreenshotHeight,comboToComboY):
                paintPixel(comboX+comboMiddleX,y+comboY,0,255,0)
    except Exception as e: 
        print(e)

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
def paintPixel(x,y,r,g,b):
        try:
            if sys.platform == "win32":
                win32gui.SetPixel(dc, x, y, win32api.RGB(r, g, b))  # draw red at x,y
            elif sys.platform == "linux" or sys.platform == "linux2":
                #linux
                print("linux not supported")
                os._exit(0)
            elif sys.platform == "darwin":
                #ios
                print("ios not supported")
                os._exit(0)
        except:
            pass

def main():
    global paused, playOnce, clickerProcess
    keySetup()
    while True:
        if clickerProcess != None and clickerProcess.is_alive():
            if not hasFinished():
                time.sleep(3)
                continue
            killClickerProcess()
        if not isStartable():
            time.sleep(1)
            continue
        if (playOnce or not paused):
            clickerProcess = mp.Process(target=launchAutoclicker,args=())
            clickerProcess.start()
            pg.click(startButtonX, startButtonY)
            playOnce = False
            time.sleep(33.1)
        time.sleep(1);
def isStartable():
    autoCalibration()
    screenshot = pg.screenshot(region=(startScreenshotCornerX, startScreenshotCornerY, 10, 1))
    for x in range(0, 10):
        r,g,b =screenshot.getpixel((x, 0))
        if r in range(0,10) and g in range(0,10) and b in range(0,10):
            if checkIfWhackPageOpenAndNotPlaying():
                print("[internal] start is available")
                return True
    return False
def hasFinished():
    screenshot = pg.screenshot(region=(comboLabelX, comboLabelY, 10, 1))
    for x in range(0, 10):
        r,g,b =screenshot.getpixel((x, 0))
        if r in range(0,10) and g in range(0,10) and b in range(0,10):
            return False
    print("[internal] game has finished")
    return True
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
        global calibrationProcess
        if calibrationProcess == None:
            print('Show calibration')
            calibrationProcess = mp.Process(target=showCalibration)
            calibrationProcess.start()
        else:
            killCalibrationProcess()

    def callbackF7(event):
         killClickerProcess()
         killCalibrationProcess()
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
def killClickerProcess():
    global clickerProcess
    if(clickerProcess != None):
        print('[internal] terminate clicker process')
        clickerProcess.kill()
        clickerProcess = None;

### START ###
if __name__ == '__main__':
    main()

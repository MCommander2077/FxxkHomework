import os
import time
import numpy as np
from PIL import ImageGrab
from PIL import Image

#主函数，会被主程序main.py调用为api
def FHScreenShot():
    global FHScreenShot_img
    #尝试截图
    try:
        ScreenShot_InProgram()
    except:
        return 'SCREENSHOT_SHOT_ERROR'
    #尝试保存
    try:
        im = Image.fromarray(FHScreenShot_img)
        im.save("screenshot.png")
    except:
        return 'SCREENSHOT_SAVE_ERROR'
    return True
    

#副函数，仅在程序内使用
#如果为程序内调试则打印日志
def OutPutLog_InProgram():
    global end,beg
    print(end - beg)
    print(FHScreenShot_img)
#截图
def ScreenShot_InProgram():
    global FHScreenShot_img,beg,end
    # 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
    beg = time.time()
    debug = False
    for i in range(10):
        FHScreenShot_img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
        FHScreenShot_img = np.array(FHScreenShot_img.getdata(), np.uint8)#.reshape(img.size[1], img.size[0], 3)
    end = time.time()
    
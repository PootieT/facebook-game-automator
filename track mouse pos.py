from ctypes import windll, Structure, c_ulong, byref
import time
import pyautogui
import math

class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

try:
	while True:
		for i in range(30):
			pos = queryMousePosition()
			im = pyautogui.screenshot()
			color = im.getpixel((math.floor(pos['x']),math.floor(pos['y'])))
			print(pos), color
			time.sleep(0.1)
except KeyboardInterrupt:
	print("interrupt")
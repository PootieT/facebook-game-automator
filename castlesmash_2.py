def get_reaction(color):
	if color_compare(color,[190,90,220]) or color_compare(color,[220,199,216]) or color_compare(color,[117,35,204]) or color_compare(color,[143,49,214]) or color_compare(color,[135,31,255]) or color_compare(color,[126,28,145]) or color_compare(color,[120,112,135])or color_compare(color,[230,220,215]):   # small mouse color and elf color
		clicks = 1
	elif color_compare(color,[251,255,111]) or color_compare(color,[240,240,90])or color_compare(color,[189,188,121]) or color_compare(color,[255,253,128]) or color_compare(color,[201,56,182]) or color_compare(color,[184,44,156]) or color_compare(color,[163,54,149])or color_compare(color,[150,145,86]) or color_compare(color,[245,212,181])or color_compare(color,[227,175,176])or color_compare(color,[245,223,203])or color_compare(color,[105,81,22]):               # the troll
		print "find troll!!!"
		clicks = 12
	elif color_compare(color,[129,126,143]) or color_compare(color,[181,119,125]) or color_compare(color,[201,56,66]) or color_compare(color,[194,126,129]) or color_compare(color,[92,78,90]) or color_compare(color,[224,135,144]) or color_compare(color,[140,133,35]) or color_compare(color,[255,120,131]) or color_compare(color,[235,45,79]) or color_compare(color,[168,158,186]) or color_compare(color,[227,204,213]):
		clicks = 1
	else:                          # otherwise dont smash the human
		clicks = 0
	if color_compare(color,[199,96,56]) or color_compare(color,[222,151,93]) or color_compare(color,[112,63,64]) or color_compare(color,[245,160,89]) or color_compare(color,[156,121,95]) or color_compare(color,[199,119,62]) or color_compare(color,[255,191,54]) or color_compare(color,[110,94,69]) or color_compare(color,[48,42,9]) or color_compare(color,[122,62,22]) or color_compare(color,[145,56,20]) or color_compare(color,[94,5,0]) or color_compare(color,[245,160,66]) or color_compare(color,[255,175,100]) or color_compare(color,[255,154,46]) or color_compare(color,[199,130,75]) or color_compare(color,[82,39,28]) or color_compare(color,[180,90,70]) or color_compare(color,[170,119,94]) or color_compare(color,[69,49,38]) or color_compare(color,[48,18,11]) or color_compare(color,[240,189,70]) or color_compare(color,[176,80,48]) or color_compare(color,[120,34,5]):  #safety for human
		clicks = 0
	return clicks

# def get_reaction(color1,color2):
# 	click = 1
# 	# if color[0] > 235 and color[1] < 230 and color[1] > 150 and color[2] > 40 and color[2] < 120:
# 	if color_compare(color1,[165,116,72]) and color_compare(color2,[18,7,10]):  #safety for human
# 		click = 0
# 	return click
def color_compare(c1,c2):
	return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)/3 < 16.5

def click(x,y):
	    win32api.SetCursorPos((x,y))
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

if __name__=='__main__':
	import math
	import pyscreenshot as ImageGrab
	import win32api, win32con
	import time
	import pyautogui

	#location of all pixels
	# locations = [[261,394],[338,394],[409,394],[255,466],[335,466],[415,466],[255,539],[333,539],[418,539]]
	# locations = [[274,385],[351,385],[422,385],[268,457],[348,457],[428,457],[268,530],[346,530],[431,530]]
	locations_top = [[257,371],[332,371],[411,371],[255,444],[331,444],[412,444],[250,517],[333,517],[415,517]]
	# locations_dark = [[261+19,394+15],[338+19,394+15],[409+19,394+15],[255+19,466+15],[335+19,466+15],[415+19,466+15],[255+19,539+15],[333+19,539+15],[418+19,539+15]]
	for playtime in range(500):
		while True:
			#screen query
			# img = ImageGrab.grab(bbox=(0,0,470,570))
			img = pyautogui.screenshot()
			# print "play again button pixel ",img.getpixel((582,364))
			# win32aimg = pyautogui.screenshot()pi.SetCursorPos((582,364))
			if color_compare(img.getpixel((364,582)),[64,128,255]):
				print "======================game ends================================="
				break
			# img.show()
			for i in range(len(locations_top)):
				# get the rgb value of that position
				color_top = img.getpixel((locations_top[i][0],locations_top[i][1]))

				# color_dark = img.getpixel((locations_dark[i][0],locations_dark[i][1]))
				print "  "
				print "location",i,"pixel color", color_top
				num_clicks = get_reaction(color_top)
			 	# then smash with the number of clicks you have
			 	print "number of clicks", num_clicks
			 	if num_clicks == 0:               #safety if human dont do it
			 		print "found human!"
			 		continue
			 	for ohoh in range(num_clicks):
			 		print "click one time"
			 		# if i == 2:
		 				# win32aimg = pyautogui.screenshot()pi.SetCursorPos((locations_top[i][0],locations_top[i][1]))
			 		click(locations_top[i][0],locations_top[i][1])
			 		# time.sleep(0.01)
			time.sleep(0.3)
		click(364,582)
		time.sleep(3.5)
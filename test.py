def get_reaction(color):
	clicks = 1
	if color_compare(color,[199,96,56]) or color_compare(color,[222,151,93]) or color_compare(color,[112,63,64]) or color_compare(color,[245,160,89]) or color_compare(color,[156,121,95]) or color_compare(color,[199,119,62]) or color_compare(color,[255,191,54]) or color_compare(color,[110,94,69]) or color_compare(color,[48,42,9]) or color_compare(color,[122,62,22]) or color_compare(color,[145,56,20]) or color_compare(color,[94,5,0]) or color_compare(color,[245,160,66]) or color_compare(color,[255,175,100]) or color_compare(color,[255,154,46]) or color_compare(color,[199,130,75]) or color_compare(color,[82,39,28]) or color_compare(color,[180,90,70]) or color_compare(color,[170,119,94]) or color_compare(color,[69,49,38]) or color_compare(color,[48,18,11]) or color_compare(color,[240,189,70]) or color_compare(color,[176,80,48]) or color_compare(color,[120,34,5]):  #safety for human
		clicks = 0
		print "found a human------------------"
	return clicks

def color_compare(c1,c2):
	return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)/3 < 16.5

def click(x,y):
	    win32api.SetCursorPos((x,y))
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def color_convert(rgb):
	return [rgb & 0xff, (rgb >> 8) & 0xff, (rgb >> 16) & 0xff]

if __name__=='__main__':
	import math
	import win32api, win32con
	import time
	from ctypes import windll
	import helper
	from sklearn import svm

	#location of all pixels
	locations_top = [[257,371],[332,371],[411,371],[255,444],[331,444],[412,444],[250,517],[333,517],[415,517]]
	hdc = windll.user32.GetDC(0)
	# for i in range(50):
	# 	baby_color.append(color_convert(windll.gdi32.GetPixel(hdc, 255,444+i)))
	# file = open("nohit.txt","a")
	# for time in range(1):
	# 	for i in range(65):
			# human_color.append(color_convert(windll.gdi32.GetPixel(hdc, 411,371-15+i)))
			# troll_color.append(color_convert(windll.gdi32.GetPixel(hdc, 415,517-15+i)))
			# color = color_convert(windll.gdi32.GetPixel(hdc, 412,444-15+i)) ## troll
			# file.write(str(color[0])+ "," +str(color[1])+ "," + str(color[2]) + "\n")
	# for i in range(50):
	# 	# human_color.append(color_convert(windll.gdi32.GetPixel(hdc, 411,371-15+i)))
	# 	# troll_color.append(color_convert(windll.gdi32.GetPixel(hdc, 415,517-15+i)))
	# 	color = color_convert(windll.gdi32.GetPixel(hdc, 411,371+i))
	# 	file.write(str(color[0])+ "," +str(color[1])+ "," + str(color[2]) + "\n")
	# file.close()	
	nohit_color = helper.read_file("nohit.txt")
	hit_color = helper.read_file("hit.txt")
	X = nohit_color + hit_color
	y = [0]*len(nohit_color) + [1]*len(hit_color)
	# then train the model
	svmModel = svm.SVC()
	svmModel.fit(X,y)
	print svmModel.predict(color_convert(windll.gdi32.GetPixel(hdc,331,444)))

def get_reaction(color):
		if color == 1 or color == 2:   # elf or small mole
			clicks = 0
		elif color == 2:               # the troll
			clicks = 3
		else:                          # otherwise dont smash the human
			clicks = 0

def click(x,y):
	    win32api.SetCursorPos((x,y))
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

if __name__=='__main__':

	import pyscreenshot as ImageGrab
	import win32api, win32con



	frame_width = 83
	frame_height = 75
	top_left_frame_x = 256
	top_left_frame_y = 504
	num_rows = 3 
	num_cols = 3 

	#screen query
	img = ImageGrab.grab()
	# img.show()
	x_pos = top_left_frame_x
	y_pos = top_left_frame_y

	for x_idx in range(num_cols):
		for y_idx in range(num_rows):
			# get the rgb value of that position
			color = img.getpixel((x_pos,y_pos))
			print "color=====", color[1]
			num_clicks = get_reaction(color)
		 	# then smash with the number of clicks you have
		 	for time in range(num_clicks):
		 		click(x_pos,y_pos)
			y_pos += frame_height
		x_pos += frame_width



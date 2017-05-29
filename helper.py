def read_file(filename):
	x = []
	file = open(filename,"r")
	for line in file:
		lst = line[0:-1].split(',')
		for i in range(3):
			lst[i] = int(lst[i])
		x.append(lst)
	return x
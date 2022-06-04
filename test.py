def drawPattern(height, width):
	for x in range(0, height):
		for y in range(0, width):
			print(' * ', end='')
		print('')
		
height = int(input("Enter the height of rectangle "))
width = int(input("Enter the width of rectangle "))
drawPattern(height , width)
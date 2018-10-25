def draw_board(size):
	v_line = ' ---'
	h_line = "|   "
 
	for i in range(1,size+1):
		print(v_line*size)
		print(h_line*(size+1))
	print(v_line*size)

if __name__ == '__main__':
	size = int(input("Enter the size of the board: "))
	draw_board(size)
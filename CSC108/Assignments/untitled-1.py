list  = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
list2 = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']]

for x in list:
	for y in x:
		print y

x = 1
y = 2

def update_board(row, column, view_board, symbol_board):
	
	view_board[row][column] = symbol_board[row][column]
def foo(x,y):
    if x != False:
	return x
    if y == ship:
	return y
    if x != False:
	return x    
    return False
	    

def reduce(foo, seq, start):
    r = start
    for item in seq:
	r = foo(r, item)

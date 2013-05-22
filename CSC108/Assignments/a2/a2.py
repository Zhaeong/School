import media
import random

# The Battleship constants.
HIDDEN = '-'
VACANT = 'X'
BOARD_SIZE = 10
SHIPS = ['A', 'B', 'C', 'D', 'E']
SIZES = [2, 3, 3, 4, 5]

# The functions that you need to implement.
# Replace pass with the function body.

def in_bounds(row, column):
    '''
    (int, int) -> bool
    Returns true if row and column are between 0 (inclusive) and BOARD_SIZE
    (non-inclusive).
    '''
    return (row >= 0 and row < BOARD_SIZE) and (column >= 0 and column < 10)

def is_win(hits_list):
    '''
    (list of ints) -> bool.
    Return True if all elements of the list are 0 or if the list is empty,
    and False otherwise.
    '''
    
    #return hits_list == [0] * len(hits_list)
    #return sum(hits_list) == 0
    
    for n in hits_list:
	if n != 0:
	    return False
    return True

def get_view_board():
    '''
    () -> list of lists of strs
    Returns a board with BOARD_SIZE rows and columns. 
    Each cell contains a HIDDEN symbol.
    '''
    
    board = []
    
    for y in range(BOARD_SIZE):
	board.append([HIDDEN] * 10) 
    return board

def get_symbol_board(filename):
    '''
    (str) -> list of lists of strs.
    Return board contained in file with given name.
    '''
    
    lines = open(filename).readlines() #list of strings
    board = []
    for line in lines:
	# line is a string of 10 meaningful chars and a newline char
	row = []
	for char in line.rstrip('\n'):
	    row.append(char)
	board.append(row)
    
    return board

def is_revealed(row, column, view_board):
    '''
    (int, int, list of list of strs) -> bool.
    Return True if cell at that row and column are not HIDDEN,and
    Return False otherwise
    '''
    return view_board[row][column] != HIDDEN

def is_occupied(row1, col1, row2, col2, board):
    '''(int, int, int, int, list of list of strs) -> bool
    returns true if the path between first int,int and second int,int is 
    not vacant, return false otherwise'''
    # path between two ints must be either horizontal or vertical, never both
    # .: difference between row/col1 or row/col2 would be 1 giving us a line
    # not a box
    for row in board[row1:row2+1]:
	for cell in row[col1:col2+1]:
	    if cell != VACANT:
		return True
    return False

def is_hit(row, column, symbol_board, hits_list):
    '''(int, int, list of lists of strs, list of ints) -> int
    returns number of hits remaining if cell at row and column contains a ship. 
    If not return -1
    '''
    # a letter representing which ship it is.
    ship = symbol_board[row][column] 

    # SHIPS will not contain it
    if ship == VACANT:
	return -1
    # The ship name must be in SHIPS .: ignore ValueError
    pos = SHIPS.index(ship)
    hits_list[pos] = hits_list[pos] - 1
    return hits_list[pos]
    

def update_board(row, column, view_board, symbol_board):
    '''(int, int, list of lists of strs, list of lists of strs) -> NoneType
    set the element of the cell at location in first value to corresponding 
    element from second list
    '''
    view_board[row][column] = symbol_board[row][column]

    
def get_num_moves(view_board):
    '''(list of lists of strs) -> int
    returns number of moves made so far for the board.
    '''
    moves = 0
    for x in view_board:
	for y in x:
	    if y != HIDDEN:
		moves += 1
    return moves
		
		
# The starter code functions.

def display_board(board):
    '''(list of list of strs) -> ()
    Display the board.'''

    # Display the column numbers
    print ' ',
    for col_num in range(BOARD_SIZE):
	print col_num,
    print 

    # Display row numbers and cell contents.
    row_num = 0
    for row in board:
	print row_num,
	for symbol in row:
	    print symbol,
	print
	row_num += 1

def place_ship(row1, col1, row2, col2, board, ship_symbol):
    '''(int, int, int, int, list of lists of strs, str) -> NoneType
    Place the ship with symbol ship_symbol on the board from (row1, col1)
    to (row2, col2).'''

    # place the ship vertically
    if (col1 == col2):
	for row in range(row1, row2):
	    board[row][col1] = ship_symbol
    
    # place the ship horizontally
    else:
	for col in range(col1, col2):
	    board[row1][col] = ship_symbol
	
	
def make_computer_board():
    '''() -> list of list of strs
    Return a new BOARD_SIZE by BOARD_SIZE board with the ships with symbols
    from SHIPS and sizes from SIZES placed either horizontally or vertically
    on the board at random locations and the rest of the spots VACANT.'''
    
    # make a BOARD_SIZE by BOARD_SIZE board that is entirely VACANT
    board = []
    for row in range(BOARD_SIZE):
	board.append([])
	for column in range(BOARD_SIZE):
	    board[row].append(VACANT)   
    
    for index in range(len(SHIPS)):
	
	# get the symbol and size of the next ship to place on the board
	placed = False
	ship = SHIPS[index]
	ship_size = SIZES[index]

	while not placed:
	    
	    # randomly generate a location at which to place the ship
	    start_row = random.randint(0, BOARD_SIZE - 1)
	    start_col = random.randint(0, BOARD_SIZE - 1)
	    
	    # randomly determine whether to place horizontally or vertically
	    direction = random.randint(0, 1)
	    
	    # determine the location for vertical placement
	    if direction == 0:
		end_row = start_row + ship_size
		end_col = start_col
		
	    # determine the location for horizontal placement
	    else:
		end_row = start_row
		end_col = start_col + ship_size
		
	    # check to see if the ship can be placed at this location
	    if in_bounds(start_row, end_row) \
	       and in_bounds(start_col, end_col)\
	       and not is_occupied(start_row, start_col, 
	                           end_row, end_col, board):
		place_ship(start_row, start_col, end_row, end_col, board, ship)
		placed = True
		
    return board
				
def make_move(view_board):
    '''(list of list of strs) -> list of ints
    Prompt the user to enter a row and column, until a pair within the range
    0 to BOARD_SIZE - 1 (inclusive) is selected and the cell at that location
    of view_board is hidden, then return a list containing that row and 
    column.'''
    
    row = int(raw_input("Please enter the row: ").strip())
    col = int(raw_input("Please enter the column: ").strip())

    while not in_bounds(row, col) or is_revealed(row, col, view_board):
	
	if not in_bounds(row, col):
	    print "Invalid cell location!  Select another cell."
	else:
	    print "That cell has already been viewed! Select another cell"
	row = int(raw_input("Please enter the row: ").strip())
	col = int(raw_input("Please enter the column: ").strip())
	
    return [row, col]

def display_hit_message(hit):
    '''(int) -> NoneType
    Display a message to the user saying whether a ship was hit, sunk, or
    missed.'''
    
    if hit > 0:
	print 'You hit a ship!  Only %d more hit(s) to sink the ship!' % (hit)
    elif hit == 0:
	print 'You sunk a ship!'
    else:
	print 'Miss!'    

def main_human_no_opponent():
    '''() -> NoneType
    A single player game with no opponent.  This exists for testing purposes.'''
	
    filename = media.choose_file()
    symbol_board = get_symbol_board(filename)
    view_board = get_view_board()
    display_board(view_board)
    hits_list = SIZES[:]
	
    while not is_win(hits_list):
		
	[row, col] = make_move(view_board)
		
	hit = is_hit(row, col, symbol_board, hits_list)
	display_hit_message(hit)
	    
	update_board(row, col, view_board, symbol_board)
	display_board(view_board)
    
    print 'You won in %d moves!' % (get_num_moves(view_board))

def make_computer_move(view_board):
    ''' (list of list of strs) -> list of ints
    Randomly generate a row and column until a cell that is still HIDDEN in 
    view_board is found, and return that row and column.'''
    
    row = random.randint(0, BOARD_SIZE - 1)    
    col = random.randint(0, BOARD_SIZE - 1)
    
    while is_revealed(row, col, view_board):
	row = random.randint(0, BOARD_SIZE - 1)    
	col = random.randint(0, BOARD_SIZE - 1)
	    
    return [row, col]

def main_human_versus_computer():
    '''() -> NoneType
    Play the game with a single player vs. the computer.'''
    	
    filename = media.choose_file()
    symbol_board_player = get_symbol_board(filename)
    view_board_player = get_view_board()
    hits_player = SIZES[:]
    
    symbol_board_computer = make_computer_board()
    view_board_computer = get_view_board()
    hits_computer = SIZES[:]
    
    player_turn = True

    while not is_win(hits_player) and not is_win(hits_computer):
		
	if player_turn:	    
	    symbol_board = symbol_board_computer
	    view_board = view_board_computer
	    print "Player 1's turn:"
	    display_board(view_board_computer)
	    [row, col] = make_move(view_board_computer)
	    hits_list = hits_player
	else:
	    symbol_board = symbol_board_player
	    view_board = view_board_player
	    print "Computer's turn: "
	    display_board(view_board_player)
	    #display_board(symbol_board_player)
	    [row, col] = make_computer_move(view_board_player)
	    hits_list = hits_computer
	    
    
	hit = is_hit(row, col, symbol_board, hits_list)
	display_hit_message(hit)
  
	update_board(row, col, view_board, symbol_board)
	display_board(view_board)
	raw_input('Please enter to continue... ')
	player_turn = not player_turn
	
    if is_win(hits_player):
	print 'You won in %d moves!' % (get_num_moves(view_board_computer))
    else:
	print 'The computer won in %d moves.  Please try again' % \
	      (get_num_moves(view_board_player))
	
	
if __name__ == '__main__':
    list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    main_human_versus_computer()
	
    # Put any code used to verify your functions here.

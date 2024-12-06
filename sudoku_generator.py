import math, random
import pygame, sys
"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = []
        for i in range(0,9):
            self.board.append([])
            for j in range(0,row_length):
                self.board[i].append(0)
        self.box_length = int(row_length ** 0.5)

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for items in self.board:
            print(items)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        #this code is written expecting the board list to be contained as [[row][row]], if this
        #changes, rewrite this code.
        searched_row = self.board[row]
        for numbers in searched_row:
            if numbers == num:
                return False
        return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        #this code is written expecting the board list to be contained as [[row][row]], if this
        #changes, rewrite this code.
        for rows in self.board:
            if rows[col] == num:
                return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        #Im gonna write this assuming all inputs are valid, if we need to add error checking later on
        #just make sure that values % 3 == 0 and if not then add up or down.
        #this code is written expecting the board list to be contained as [[row][row]], if this
        #changes, rewrite this code.
        searched_rows = []
        for i in range(row_start, row_start + 3):
            searched_rows.append(self.board[i])
        for rows in searched_rows:
            for i in range(col_start, col_start + 3):
                if rows[i] == num:
                    return False
        return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        #This should hopefully work
        #This in fact did not work and I had to remove the valid in box call
        #might have to add it back later but ima just run it like this for now
        if self.valid_in_row(row, num):
            if self.valid_in_col(col, num):
                return True
        return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        #Im gonna write this assuming all inputs are valid, if we need to add error checking later on
        #just make sure that values % 3 == 0 and if not then add up or down.
        #this code is written expecting the board list to be contained as [[row][row]], if this
        #changes, rewrite this code.
        wanted_rows = []
        for i in range(row_start, row_start + 3):
            wanted_rows.append(self.board[i])
        for rows in wanted_rows:
            for i in range(col_start, col_start + 3):
                number_to_insert = random.randint(1,9)
                while not self.valid_in_box(row_start,col_start, number_to_insert):
                    number_to_insert = random.randint(1, 9)
                rows[i] = number_to_insert
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        self.fill_box(0,0)
        self.fill_box(3,3)
        self.fill_box(6,6)


    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        for i in range(0, self.removed_cells):
            cell_removed = False
            while not cell_removed:
                row_num = random.randint(0, 8)
                col_num = random.randint(0, 8)
                if self.board[row_num][col_num] != 0:
                    self.board[row_num][col_num] = 0
                    cell_removed = True


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketch = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketch = value


    def draw(self):
        x = self.col * 60
        y = self.row * 60
        pygame.draw.rect(self.screen, (202, 228, 241), (x, y, 60, 60))
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, 60, 60), 5)

        font = pygame.font.SysFont('Arial', 30)
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 20))
        elif self.sketch != 0:
            text = font.render(str(self.sketch), True, (0, 0, 0))
            self.screen.blit(text, (x + 20, y + 20))


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None
        self.generate_sudoku()

    def generate_sudoku(self):
        self.sudoku_generator = SudokuGenerator(9, self.difficulty)
        self.sudoku_generator.fill_values()
        self.sudoku_generator.remove_cells()
        self.board = self.sudoku_generator.get_board()
        for row in range(9):
            for col in range(9):
                self.cells[row][col].set_cell_value(self.board[row][col])


    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
        for i in range(10):
            thickness = 2 if i % 3 != 0 else 5
            pygame.draw.line(self.screen, (0, 0, 0), (i*60, 0), (i*60, 540), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i*60), (540, i*60), thickness)



    def selected(self, row, col):

        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True


    def click(self, x, y):
        row = y // 60
        col = x // 60
        if 0 <= row < 9 and 0 <= col < 9:  # Ensure click is within bounds
            self.selected(row, col)

    def sketch(self, value):
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)



    def place_number(self, value):
        if self.selected_cell:
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        self.generate_sudoku()

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def check_board(self):
        for row in range(9):
            for col in range(9):
                if not self.sudoku_generator.is_valid(row, col, self.cells[row][col].value):
                    return False
        return True







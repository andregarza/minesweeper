from tkinter import *
from functools import partial
import numpy as np 

class Minesweeper:

    # Method to define the instance of the object
    def __init__(self, bombs = 2):

        self.bombs = bombs

    # Method to create the array with the bomb coordinate  
    def bombs_place(self):

        # input the number of bombs
        #self.bombs = int(input("Cuantas bombas quieres  "))
        self.bombs = 4
        # Generating the array for the bomb coordinates
        self.bomb_list = np.random.randint(low = 0, high = 5, size = (self.bombs,2))
        return self.bomb_list

    # Method to create the empty array and place the bombs in the board
    def board_creation(self):
        
        #Create the array of zeros
        self.board = np.zeros([5, 5], dtype=int)
        # Place bombs in the array
        for i in self.bomb_list:
            self.board[i[0]][i[-1]] = 10
        # iterate the array 
        for x in range(5):
            for y in range(5):
                # Checks for bombs and update every tile acordingly to how many bombs are sorrounding the tile 
                if self.board[x][y] == 10:
                    try:
                        # Checks if the substraction is greater than 0 to avoid moving to the last element of the array 
                        if y - 1 > 0:
                            # Avoids adding to a bomb tile
                            if not self.board[x - 1][y - 1] == 10:
                                # adds to the tile
                                self.board[x - 1][y - 1] += 1                                              
                    except:
                        pass       
                    try:
                        if y -1 >= 0:
                            if not self.board[x][y - 1] == 10:
                                self.board[x][y - 1] += 1 
                             
                    except:
                        pass     
                    try:
                        if y - 1 >= 0:
                            if not self.board[x + 1][y - 1] == 10:
                                self.board[x + 1][y - 1] += 1
                    except:
                        pass     
                    try:
                        if x - 1 >= 0:
                            if not self.board[x - 1][y] == 10: 
                                self.board[x - 1][y] += 1
                    except:
                        pass     
                    try:
                        if not self.board[x + 1][y] == 10: 
                            self.board[x + 1][y] += 1
                    except:
                        pass     
                    try:
                        if x - 1 >= 0:
                            if not self.board[x - 1][y + 1]:
                                self.board[x - 1][y + 1] += 1
                    except:
                        pass     
                    try:
                        if not self.board[x][y + 1] == 10:
                            self.board[x][y + 1] += 1
                    except:
                        pass     
                    try:
                        if not self.board[x + 1][y + 1] == 10 : 
                            self.board[x + 1][y + 1] += 1
                    except:
                        pass                              
     
        return self.board    
    # Class to create the board
    class MainFrame(Frame):
        coordinates = 0
    # define the class
        def __init__(self, parent):
            super().__init__()
            # Creates a loop and creates every button 
            for row in range(0, 5): 
                for column in range(0, 5):
                    new_button = Button(self, width= 5, height= 3, text="")
                    new_button.grid( row=row, column=column, sticky=N+S+E+W )
                    new_button["command"] = partial(self.press, new_button, row, column) # uses the partial to use the coordinates in the press function

        # This function gives the button their functionality
        def press(self, btn, row, col):
            coordinates = (row, col)
            print(coordinates)
            btn.configure(bg="grey", text="hola")
            btn.configure(activebackground="grey")

   

    if __name__ == "__main__":
        root = Tk()
        root.title("Minesweeper")
        root.resizable(True, True)
        MainFrame(root).pack(side="top", fill="both", expand=True)
        root.mainloop()





new_game = Minesweeper()
print(new_game.bombs_place())
print(new_game.board_creation())




    



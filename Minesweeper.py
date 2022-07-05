import numpy as np 

class Minesweeper:

    # Method to define the instance of the object
    def __init__(self, bombs = 2):

        self.bombs = bombs

    # Method to create the array with the bomb coordinate  
    def bombs_place(self):

        # input the number of bombs
        self.bombs = int(input("Cuantas bombas quieres  "))
        # Generating the array for the bomb coordinates
        bomb_list = np.random.randint(low = 0, high = 10, size = (self.bombs,2))
        return bomb_list



new_game = Minesweeper()
print(new_game.bombs_place())


    



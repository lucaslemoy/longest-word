import string
import random
class Game:
    def __init__(self):
        self.grid = []
        self.word = ''
        for _ in range(0,9):
            self.grid.append(random.choice(string.ascii_uppercase))
    def is_valid(self,word):
        if word == '':
            return False
        grid_copy=self.grid.copy()
        for letter in word:
            if letter in grid_copy:
                grid_copy.remove(letter)
            else :
                return False
        return True


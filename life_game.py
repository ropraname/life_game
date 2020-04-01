#Саргин Ярослав
import copy


EMPTY = 0
ROCK = 1
FISH = 2
SHRIMP = 3

class LifeGame(object):
    """
    Class for Game life
    """
    def __init__(self, table):
        self.earth = copy.deepcopy(table)
        self.copy_earth = copy.deepcopy(table)
        
    def _getNeighbours(self, height, length):
        self.neighbours = []

        BACK_L, BACK_H = 1, 1
        NEXT_L, NEXT_H = 2, 2
        if height == 0: BACK_H = 0
        if length == 0: BACK_L = 0
        if height == len(self.copy_earth) - 1: NEXT_H = 1
        if length == len(self.copy_earth[0]) - 1: NEXT_L = 1

        for ch_height in range(height - BACK_H, height + NEXT_H):
            for ch_length in range(length - BACK_L, length + NEXT_L):
                if [ch_height, ch_length] != [height, length]:
                    self.neighbours.append(self.copy_earth[ch_height][ch_length])
        self.fish = self.neighbours.count(FISH)
        self.shrimp = self.neighbours.count(SHRIMP)

    def _prepare_to_get_next_generation(self):
        for height in range(len(self.earth)):
            for length in range(len(self.earth[0])):

                if self.earth[height][length] == ROCK:
                    continue
                else:
                    self._getNeighbours(height, length)

                    if self.copy_earth[height][length] == FISH and self.fish < 2:
                        self.earth[height][length] = EMPTY
                        continue

                    if self.copy_earth[height][length] == SHRIMP and self.shrimp < 2:
                        self.earth[height][length] = EMPTY
                        continue

                    elif self.fish == 2 and self.shrimp == 2: continue

                    elif self.fish == 3:
                        self.earth[height][length] = FISH
                        continue
                    elif self.shrimp == 3:
                        self.earth[height][length] = SHRIMP
                        continue

                    elif self.fish > 3: 
                        self.earth[height][length] = EMPTY
                        continue
                    elif self.shrimp > 3:
                        self.earth[height][length] = EMPTY
                        continue
                        
    def get_next_generation(self):
        self._prepare_to_get_next_generation()
        self.copy_earth = copy.deepcopy(self.earth)
        return self.earth

import math
class Allergies(object):
    allergant = {
        0: 'eggs',
        1: 'peanuts',
        2: 'shellfish',
        3: 'strawberries',
        4: 'tomatoes', 
        5: 'chocolate',
        6: 'pollen',
        7: 'cats',
    }

    def find_allergant(self, score):
        score = score % 256
        allergant_list_index = []
        index = 7
        while score > 0:
            if score & (1<<index):
                allergant_list_index.append(self.allergant[index])
                score -= 1<<index
            index -= 1
        return allergant_list_index
    
    def __init__(self, score):
        self.allergant_list = self.find_allergant(score)

    def is_allergic_to(self, item):
        return item in self.allergant_list

    @property
    def lst(self):
        return self.allergant_list
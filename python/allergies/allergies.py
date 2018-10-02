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
        return [index for index in range(7,-1,-1) if score & (1<<index)]
    
    def __init__(self, score):
        self.allergant_list_index = self.find_allergant(score % 256)

    def is_allergic_to(self, item):
        return [key for key, value in self.allergant.items() if value == item][0] in self.allergant_list_index

    @property
    def lst(self):
        return [self.allergant[item] for item in self.allergant_list_index]
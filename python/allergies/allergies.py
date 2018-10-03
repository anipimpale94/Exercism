import math
class Allergies(object):
    allergant = {
        1:'eggs', 2:'peanuts', 4:'shellfish', 8:'strawberries', 16:'tomatoes', 32:'chocolate', 64:'pollen', 128:'cats',
    }
    allergant_rev = {
        'eggs':1, 'peanuts':2 , 'shellfish':4, 'strawberries':8, 'tomatoes':16, 'chocolate':32, 'pollen':64, 'cats':128,
    }

    def find_allergant(self, score):
        return [1<<index for index in range(7,-1,-1) if score & (1<<index)]
    
    def __init__(self, score):
        self.score = score % 256
        self.allergant_list = self.find_allergant(self.score)

    def is_allergic_to(self, item):
        # return [key for key, value in self.allergant.items() if value == item][0] in self.allergant_list
        return bool(self.allergant_rev[item] & self.score)


    @property
    def lst(self):
        return [self.allergant[item] for item in self.allergant_list]
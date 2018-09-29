import math
class Allergies(object):

    def nearest_power_of_2(self, value):
        return 2 ** int(math.log(value,2))

    def get_allergant_name(self, value):
        if value == 1: return 'eggs'
        elif value == 2: return 'peanuts'
        elif value == 4: return 'shellfish'
        elif value == 8: return 'strawberries'
        elif value == 16: return 'tomatoes'
        elif value == 32: return 'chocolate'
        elif value == 64: return 'pollen'
        elif value == 128: return 'cats'

    def make_list(self, score):
        allergant_list = []
        while score > 1:
            nearest_score = self.nearest_power_of_2(score)
            allergant_list.append(self.get_allergant_name(nearest_score))
            score = score - nearest_score
        if score == 1:
            allergant_list.append('eggs')
        return list(filter(None.__ne__, allergant_list))
    
    def __init__(self, score):
        self.allergant_list = self.make_list(score)

    def is_allergic_to(self, item):
        if item in self.allergant_list:
            return True
        else:
            return False

    @property
    def lst(self):
        return self.allergant_list


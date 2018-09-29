import math
class Allergies(object):

    def get_allergant_name(self, value):
        if value == 0: return 'eggs'
        elif value == 1: return 'peanuts'
        elif value == 2: return 'shellfish'
        elif value == 3: return 'strawberries'
        elif value == 4: return 'tomatoes'
        elif value == 5: return 'chocolate'
        elif value == 6: return 'pollen'
        elif value == 7: return 'cats'

    def make_allergant_list(self, index_list):
        for index,item in enumerate(index_list):
            index_list[index] = self.get_allergant_name(item)
        return index_list

    def find_allergant(self, score):
        score = score % 256
        allergant_list_index = []
        index = 7
        while score > 0:
            remainder = score % (1<<index)
            if score != remainder:
                allergant_list_index.append(index)
                score = remainder
            index -= 1
        return self.make_allergant_list(allergant_list_index)
    
    def __init__(self, score):
        self.allergant_list = self.find_allergant(score)

    def is_allergic_to(self, item):
        return item in self.allergant_list

    @property
    def lst(self):
        return self.allergant_list
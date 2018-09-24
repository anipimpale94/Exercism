import math
def primitive_triplets(number_in_triplet):
    pass


def triplets_in_range(range_start, range_end):
    pass


def is_triplet(triplet):
    if len(triplet) == 3:
        c = max(triplet)
        sum = 0
        for index in range(0,3):
            if(triplet[index] != c):
                sum = sum + triplet[index]**2
        if c**2 == sum:
            return True
        else:
            return False
    else:
        raise ValueError("Invalid Input")


from numpy import prod
from functools import reduce 
from math import gcd 
import itertools
def sum_of_multiples(limit, multiples):
    return sum([calculate_sum_per_multiple(limit-1, multiple) for multiple in multiples]) - sum([calculate_sum_per_multiple(limit-1, item) for item in lcm_of_2(multiples)]) + (calculate_sum_per_multiple(limit-1, lcm_of_3(multiples)) if len(multiples) > 2 else 0)

def calculate_sum_per_multiple(limit, multiple):
    return int(multiple * (0.5 * int(limit/multiple) * (int(limit/multiple)+1)))

def lcm_of_2(numbers):
    return list(set([reduce(lambda a,b: a*b // gcd(a,b), item) for item in list(itertools.product(numbers,numbers)) if item[0] != item[1]]))

def lcm_of_3(numbers):
    return reduce(lambda a,b: a*b // gcd(a,b), numbers)

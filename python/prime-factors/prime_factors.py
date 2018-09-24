import math
def prime_factors(natural_number):
    n = natural_number
    primeFactor = []
    if natural_number < 2: 
        return primeFactor
    else:
        while n%2 == 0:
            n=n/2
            primeFactor.append(2)
        
        for index in range(3, int(math.sqrt(natural_number))+1):
            while n%index == 0:
                n=n/index;
                primeFactor.append(index)
            index = index + 2
        
        if n > 2:
            primeFactor.append(n)
    return primeFactor

prime_factors(9)

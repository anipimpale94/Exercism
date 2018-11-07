import math
def primitive_triplets(number_in_triplet):
    if number_in_triplet % 2 == 1:
        raise ValueError("Odd number")
    c = 0
    m = 2
    triplet = []
    while c < number_in_triplet**3:
        for n in range(1,m):
            a = m * m - n * n
            if a == number_in_triplet:
                continue
            b = 2 * m * n 
            c = m * m + n * n
            if a == number_in_triplet or b == number_in_triplet or c == number_in_triplet:
                if c > number_in_triplet**3:
                    break           
                triplet.append(tuple(sorted((a, b, c))))
                
        m = m + 1
    return triplet


def triplets_in_range(range_start, range_end):
    c = 0
    m = 2
    triplet = []
    while c < range_end:
        for n in range(1,m):
            a = m * m - n * n
            b = 2 * m * n 
            c = m * m + n * n
            if a >= range_start and b >= range_start and c >= range_start:
                if c > range_end:
                    break           
                triplet.append(tuple(sorted((a, b, c))))
        m = m + 1
    return triplet


def is_triplet(triplet):
    if len(triplet) == 3:
        c = max(triplet)
        sum = 0
        for index in range(0,3):
            if triplet[index] != c:
                sum = sum + triplet[index]**2
        return c**2 == sum
    else:
        raise ValueError("Invalid Input")

print(triplets_in_range(56, 95))
# print(primitive_triplets(288))
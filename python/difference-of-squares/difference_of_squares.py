def square_of_sum(count):
    sum = 0
    for x in range(0, int(count)+1):
        sum = sum + x
    return sum*sum

def sum_of_squares(count):
    sum = 0
    for x in range(0, int(count)+1):
        sum = sum + x*x
    return sum

def difference(count):
    return abs(sum_of_squares(count) - square_of_sum(count))

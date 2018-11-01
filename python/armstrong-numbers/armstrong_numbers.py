def is_armstrong(number):
    return True if sum([int(i)**len(str(number)) for i in str(number)]) == number else False

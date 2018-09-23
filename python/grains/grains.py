def on_square(integer_number):
    if integer_number > 0 and integer_number < 65:
        return pow(2, integer_number-1)
    raise ValueError("Invalid Input")

def total_after(integer_number):
    if integer_number > 0 and integer_number < 65:
        sum = 1
        for index in range(1,integer_number):
            sum = sum + pow(2, index)
        return sum    
    raise ValueError("Invalid Input")

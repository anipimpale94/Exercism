def on_square(integer_number):
    if integer_number > 0 and integer_number < 65:
        return 1<<integer_number-1
    else:
        raise ValueError("Invalid Square")


def total_after(integer_number):
    if integer_number > 0 and integer_number < 65:
        return (1<<(integer_number)) - 1
    else:
        raise ValueError("Invalid Square")
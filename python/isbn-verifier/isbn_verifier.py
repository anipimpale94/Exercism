def calculateISBN10(isbn):
    sum = 0
    for index, item in enumerate(isbn):
        if item.isdigit():
            sum = sum + int(item) * (10 - index)
        else:
            if item == 'X':
                sum = sum + 10   
    return sum


def verify(isbn):
    preProcessedISBN = isbn.replace('-', '')
    if len(preProcessedISBN) == 10 and preProcessedISBN[:-1].isdigit():
        sumResult = calculateISBN10(preProcessedISBN)
        if sumResult % 11 == 0:
            return True
    return False



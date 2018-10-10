def sum_of_multiples(limit, multiples):
    values = []
    for item in multiples:
        for item in range(item,limit, item):
            values.append(item)
    return sum(set(values))

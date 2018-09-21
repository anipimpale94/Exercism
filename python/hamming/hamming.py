def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) == len(strand_b):
        for index, item in enumerate(strand_a):
            if( item != strand_b[index]):
                count = count + 1
        return count
    else:
        raise ValueError("DNA strand doesn't match size doesnt match")


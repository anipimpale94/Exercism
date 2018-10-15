def sum_of_multiples(limit, multiples):
	values = set()
	for item in multiples:
		values.update(range(item, limit, item))

	return sum(values)

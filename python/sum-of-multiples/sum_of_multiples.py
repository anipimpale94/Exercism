def sum_of_multiples(limit, multiples):
	values = set()
	for item in multiples:
		for index in range(item, limit, item):
			values.update([index])

	return sum(values)

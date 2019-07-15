def too_old(x):
	return x > 30
ages = (22, 25, 29, 24, 56, 34, 12)
print(list(filter(too_old, ages)))

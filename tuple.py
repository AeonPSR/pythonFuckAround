list = [(2, 5), (4, 8, 9), (0, 3), (7, 8, 12, 0)]

i = 0
for x in list:
	print(f"{list[i]}")
	i = i+1

tuples_inverse =  [tuple(reversed(z)) for z in list]

print(f"{tuples_inverse}")

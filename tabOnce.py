lsInput = [1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8]
lsOut = []

for x in lsInput:
	if lsInput[x] not in lsOut:
		lsOut.append(lsInput[x])

print(f"{lsOut}")
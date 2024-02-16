width = int(input("Size of the pyramid: "))

stars = 1

while width > 0:
	temp = 0
	while temp < width-1:
		print(f" ", end='')
		temp += 1
	temp = 0
	while temp < stars:
		print(f"*", end='')
		temp += 1
	print(f" ")
	stars += 1
	width -= 1
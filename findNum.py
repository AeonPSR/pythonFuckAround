import random

lives = int(input("Number of tries: "))
nbr = random.randint(1, 100)

print(f"Find the number between 1 and 100.")
while (lives > 0):
	print(f"{lives} tries remaining.")
	value = int(input("Guess a number: "))
	if (value == nbr):
		break
	if (value > nbr):
		print(f"Too high.")
	if (value < nbr):
		print(f"Too low.")
	lives -= 1
if (lives == 0):
	print(f"\nYou failed.")
	print(f"The number was {nbr}.")
else:
	print(f"\nWell done.")
	print(f"The number was {nbr}.")
print(f"There was {lives} tries left.")

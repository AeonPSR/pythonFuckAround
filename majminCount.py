sentence  = input("Input: ")
maj = 0
min = 0

for char in sentence:
	if char.isupper():
		maj += 1
	if char.islower():
		min += 1
print(f"String: {sentence}")
print(f"Uppercase: {maj}")
print(f"Lowercase: {min}")
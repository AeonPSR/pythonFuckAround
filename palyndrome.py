def palyndromes(list):
	count = 0

	for i in list:
		for c in list[i]:
			word = list[i:c]
			if word == word[::-1]:
				count += 1
	return count


print(f"{palyndromes('coiffeur, kayak, blabla, bidule, machin, yuioiuy')}")
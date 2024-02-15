def nameExtraction(list, index):
	if index > len(list) or index < 1:
		return 0
	return lsInput[index]

lsInput = ["Malek", "Nagaakira", "Mitsuakira", "Tsunaakira", "Tsunanaga"]
print(f"{nameExtraction(lsInput, 8)}")
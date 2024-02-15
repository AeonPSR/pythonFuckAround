txt = "Malek est un vrai samourai"
list = txt.split(" ")
print(f"Number of words: {len(list)}")
string = ' '.join(list)
print(f"String: {string}")
if "bonjour" in txt:
	print(f"Bonjour est dans la variable.")
else:
	print(f"Bonjour n'est pas dans la variable.")

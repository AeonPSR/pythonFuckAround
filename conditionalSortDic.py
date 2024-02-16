dic = {'a': 15, 'b': 2, 'c': 18, 'd': 12}

sort = {key: value for key, value in dic.items() if value > 14}

print(f"Sorted Dictionary: {sort}")
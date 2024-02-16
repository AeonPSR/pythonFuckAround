dic = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

sort = dict(sorted(dic.items(), key=lambda item: item[1]))

print(f"Sorted Dictionary: {sort}")
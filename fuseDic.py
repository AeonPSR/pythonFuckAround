dic1 = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "GPA": 3.8
}

dic2 = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
    "year_published": 1960
}

dic3 = {}
dic3.update(dic1)
dic3.update(dic2)

print(f"Fused Dictionary: {dic3}")
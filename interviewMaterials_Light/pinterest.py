input = ["animal", "books", "person", "dog"]
# outcome = 'animal, books, person, and dog'
i = 0

while i < len(input):
    emptyStr = ""
    if i == 3:
        emptyStr += "and" +" "+ input[i]
    else:
        emptyStr += input[i]
    i +=1
    print(emptyStr)
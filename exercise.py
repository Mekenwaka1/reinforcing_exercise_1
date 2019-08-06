
dictionary = {}

for index in range(1,51):
    # print(index)
    if index % 2 == 0 and index % 7 == 0:
        dictionary[index] = index * 2
    elif index % 2 == 0:
        dictionary[index] = index + 1
    elif index % 7 == 0:
        dictionary[index] = index - 1
    else:
        dictionary[index] = index 

print(dictionary)
    
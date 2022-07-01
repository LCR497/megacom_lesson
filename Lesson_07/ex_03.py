dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
for i in dict1.keys():
    if dict1.get(i) % 3 == 0:
        dict1.update(i='Hi')
    elif dict1.get(i) % 5 == 0:
        dict1.update(i = 'Bye')
print(dict1)

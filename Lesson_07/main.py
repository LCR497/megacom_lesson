#Problem 1
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(6)
print(dates_of_birth)

#Problem 2
a = frozenset()
a = {1,234,3,4}
b = frozenset()
b ={3,4,78,43}
c = set()
c.update(a,b)
print(c)

#Problem3
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_1.difference(farm_2)
print(farm_1)

#Problem4
a = {'2','aman','r',3,10}
a.add(13)
print(a)
a.pop()
print(a)

#Problem5
# l = set()
# for i in range(10):
#     number = int(input('Enter the number'))
#     l.add(number)
# c = frozenset()
# c = l
# print(c)

#Problem6
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
farm_3 = set()
farm_4 = set()
farm_3 = farm_1.intersection(farm_2)
farm_4 = farm_1.difference(farm_2)
print(farm_3)
print(farm_4)


#Problem7
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update(drinks = ['Coca-Cola', 'Sprite', 'Fanta'])
print(menu)

#Poblem8


languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	if i == 'php':
		break

#Problem02

a = 7
for i in range(5):
	a *= a
print(a)


#Problem03
a = 0
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
	print(f'{a} {i}')
	a += 1

#Problem04
status = True
i = 0
a = 0
while a <= 18:
	if status is True:
		i+=1
		print(i)
		if i==10:
			status = False
	else:
		i-=1
		print(i)
	a+=1

#Problem06
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(len(names)):
	if i%2 == 0:
		print(names[i])

#Problem07

for i in range(1,13,2):
	print(names[i])

#Problem08

b = int(input('input: '))
if 100<=b<=999:
	print('Это число трёхзначное')
elif b>0 and a%2==0:
	print('Это число положительное и чётное')
elif b%31==0:
	print('Это число делится на 31 без остатка')
elif (b>100 and b%17==0) or (b>150 and  b == 13**2):
	print(b)


#Problem09
k = []
g = []
for i in range(-100,100):
	if i % 13 == 0:
		print('I**2 = ', i**2)
		k.append(i)
for i in range(-100,100,7):
	if i % 2 != 0:
		print(i)
		g.append(i)
print('Firs list: ', len(k))
print('Second list: ', len(g))

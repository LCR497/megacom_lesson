#Problem01
a = []
a.append('123')
a.append(12)
a.append(1.32)
a.append(True)
a.append('123')

#Problem02
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson',
         'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack',
         'Jimmy', 'Jack', 'Jackson', 'Jhon',]
c=0
for i in names:
    if i == 'Jack':
        c+=1
print(c)

#Problem03
# for i in range(len(names)):
#     if i % 2 == 0:
#         names.pop(i+1)
# print(names)

#Problem04
ok_list = []
ok_list.append('Aman')
ok_list.append(1999)
ok_list.append('Python')

#Problem05
names = ['Aman','Nurtay','Erlan','Dastan','Kairat']
name = ''.join(names)
print(name)
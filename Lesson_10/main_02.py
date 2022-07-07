#1Напишите код где есть TypeError,IndexError,NameError.
try:
    print(1+'b')
except TypeError as t:
    print('Error of T')
a = [0,1]
try:
    print(a[3])
except IndexError as t:
    print('Error of G')

try:
    print(name)
except NameError as t:
    print('Error of F')

#2Возьмите код #1 и создайте для него try... except... Создайте несколько except выражений для разных типов ошибок.
try:
    at = 10
    inm = 15
    wo = 20
    for e in range(-at, at):
        print(wo / e)
        if at > 5:
            print("at > 5")
except (SyntaxError, IndexError,ZeroDivisionError) as e :
    print('SyntaxError')

#Перенесите к себе код #2 и исправьте все ошибки, сделайте так чтобы работал. Если не знаете как исправить ошибку создайте для неё except выражение.
lst = []
for i in range(10):
    lst.append(i)
    a = list(reversed(lst))
    sls_obj = slice('0','8')
    print(list[sls_obj])

#Перенесите к себе код #2 и исправьте все ошибки, сделайте так чтобы работал. Если не знаете как исправить ошибку создайте для неё except выражение

print(1+ord('b'))
print(a[1])
name = 'Aman'
print(name)


a = 0
b = 1
numbers = []
while b > a:
    numbers.append(b)
    b += 1
print(numbers)
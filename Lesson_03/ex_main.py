#Problem1
a = 2**3
b = 3**2
if a > b:
    print(a)
else:
    print(b)

#Problem2
a = 10
b = 20
c = 30
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

#Problem3

a = 17391 % 17
b = 564 % 17
c = 934 % 17
if a > b and a > c:
   print(a)
elif b > a and b > c:
   print(b)
else:
   print(c)

#Problem4

x = 13**2
y = 172
if x > y:
    print('x bolwe')
else:
    if x**2 > y:
         print('x**2 bolwe')


#Problem5
a = int(input('vedite chislo: '))
if a%2 == 0 and a%3 == 0 and a**2 > 1000:
    print('vse uslovia vypulneny')
else:
    print('chislo ne prowlo')

#Problem6
a = int(input('input number: '))
if 0 <= a <= 21 or 57<=a<=100:
    print('is correct')
else:
    print('no correct')

#Problem 7

a = 100
if a < 100:
    print('pass')
elif a <= 100:
    print('correct')
else:
    print('no')

#Problem8
score = 20
money = 1000
x = 50
if score > 10:
    if money > 900:
        if x > 49:
             print('good')
else:
    print('bad')

#Problem9

a = 10//5
b = 10/5
if a == b:
    print('sum of a+b: ', a+b)
else:
    print('ne ravno')


#Problem10
a = int(input('vvedite chislp: '))
if a< 0:
    print('eto chislo otizatelnoe')
else:
    print('eto chislo polojitelnoe')


#Problem11

a = 10
b = 5
if a > 0 and b > 0:
    print('good')
else:
    print('bad')

#Problem12

if a > b:
    print('a>b',a+2)
else:
    print('b>a',b+2)



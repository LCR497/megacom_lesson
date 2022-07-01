y = int(input('1.python\n 2.java\n 3.javascript\n '))
age = int(input('age: '))
o = int(input('oput: '))
salary = int(input('salary: '))

if y==1 or y==2 or y==3 and 18<=age<=65 and o>=3 and salary <= 60000:
    print('yes')
else:
    print('no')


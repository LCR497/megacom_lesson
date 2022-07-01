import random
n = random.randint(1, 100)
print(n)
m = 0
while m <= 10:
    l = int(input('Enter number --> '))
    if l == n:
        print('Okey, you won!')
        break
    elif l >= n:
        print('This number is greater')
    else:
        print('This number is less')
    m+=1
summ = 0
m = 0
pr = 0
while m <=12:
    money = int(input('Vnosim ->'))
    if money <= 100000:
        summ += money
        m+=1
        if m == 6 or m == 12:
            summ = summ * 0.1
            pr += 0.1
    else:
        break
print(summ)
print(f'{pr*100} %')

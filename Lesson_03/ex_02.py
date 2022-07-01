r = int(input('Vedite chislo esli vy hotite: \n 1.Chon aryk\n 2.baytik\n 3.Orti-sai'))
k = bool(input('Esli iz kirpicha to TRUE'))
p = bool(input('Esli iz peskobloka to TRUE'))
s = int(input('sotyx: '))
money = int(input('money: '))
if r == 1 or r == 2 or r == 3:
    if k is True and s<=4:
        if money <= 50000:
            print('kupili dom iz kirpicha')
elif r==1 or r==3 or r==3:
    if p is True and s<=5:
        if money <= 45000:
            print('kupili dom iz peskobloka')
else:
    print('nichego ne kupili')


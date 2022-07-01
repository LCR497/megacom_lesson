ram = int(input('RAM: '))
ssd = int(input('SSD: '))
hdd = int(input('HDD: '))
money = int(input('Money: '))
if 4<=ram<=8 and ssd>=256 and hdd>=1 and money<=1000:
    print('kupim')
else:
    print('ne kupim')


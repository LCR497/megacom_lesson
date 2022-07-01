cars = input('choice your model car: ')
year = int(input('year: '))
probeg = int(input('probeg: '))
color = input('choice your color: ')
rule = input('left or right: ')
hoz = int(input('Hozyain: '))
money = int(input('money: '))

if cars == 'lexus' or cars == 'toyota' and probeg <= 150000 and color == 'gray' or color == 'white' and rule == 'left' and hoz <= 2 and money <= 10000:
    print('kuplu')
elif cars == 'lexus' or cars == 'toyota' and probeg <= 200000 and color == 'gray' or color == 'white' and rule == 'left' and hoz <= 2 and money <= 8000:
    print('kupli toje')
else:
    print('ne kuplu')

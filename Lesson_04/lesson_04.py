
#Problem01

text = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
print(text.count(' '))

#Problem02

text02 = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'"
i = text02.split(' ')
print(i)
for a in i:
    if a.isalpha():
        print('String')
    else:
        print('integer')

#Problem03

text03 = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
print(text03.title())

#problem04

text_ex = 'GitHub'
user = str(input('enter the symbol: '))
print(text_ex.split(user))

#Problem05

text_04 = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
print(text_04.replace('Е','3'))

#Problem06

i = len(text_04)
p = int(i/2)
a = text_04[:p]
b = text_04[p:]
print(a.upper())
print(b.lower())

if i > 0:
	print('Aman is great')

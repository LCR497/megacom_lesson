while True:
    menu = input('Choose operation: ')
    if menu == '*':
        a = int(input('First number: '))
        b = int(input('Second number: '))
        print(f'result: {a} * {b} = {a*b}')
    elif menu == '-':
        a = int(input('First number: '))
        b = int(input('Second number: '))
        print(f'result: {a} - {b} = {a - b}')
    elif menu == '+':
        a = int(input('First number: '))
        b = int(input('Second number: '))
        print(f'result: {a} + {b} = {a + b}')
    elif menu == '/':
        a = int(input('First number: '))
        b = int(input('Second number: '))
        if b == 0:
            print("You can't divide by zero")
        else:
            print(f'result: {a} / {b} = {a/b}')
    elif menu == '0':
        print('Calculator closed')
        break
    else:
        print('No such operation exists.')
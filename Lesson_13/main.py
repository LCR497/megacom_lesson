#task1
values = ("turusbekova 109/1", 10, 1005, ["tables", "chairs"], 23.00)
def convert(c):
    arr = []
    for i in c:
        if type(i) == int or type(i) == str or type(i) == tuple or type(i) == dict:
            arr.append(True)
        else:
            arr.append(False)
    if all(values) == True:
        print('Yes')
    else:
        print('No')
convert(values)

#task2

def add_and_min():
    set_ = set()
    for i in range(0,5):
        number = int(input('Enter the number: '))
        set_.add(number)
    print(min(list(set_)))

# add_and_min()

#task3

try:
    a = eval(input('Python ФУНКЦИЮ: '))
except (NameError,SyntaxError) as n:
    print('Python такой функции нет!')

#task4
def bank(summa):
    if summa >= 50000:
        result = summa * (3.47 / 100)
        print(round(result,2))
bank(60000)


#task5


def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print(add(1,2))
print(substract(1,2))
print(multiply(1,2))
print(divide(1,2))

#task6

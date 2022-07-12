#Task 2
def square_number(num):
    return num ** 2
def test_square_number():
  assert square_number(2) == 4
  assert square_number(8) == 64
  assert square_number(10) == 100
  print("YOUR CODE IS CORRECT!")
test_square_number()


#Task 3
def is_odd(num):
    return num % 2 != 0
def test_is_odd():
  assert is_odd(2) == False
  assert is_odd(3) == True
  assert is_odd(8) == False
  assert is_odd(100) == False
  assert is_odd(101) == True
  print("YOUR CODE IS CORRECT!")
test_is_odd()

#Task 4

def last_letter(word):
    arr = [i for i in word]
    arr.reverse()
    return str(arr[0])
def test_last_letter():
  assert last_letter('hello!') == '!'
  assert last_letter('banana') == 'a'
  assert last_letter('8') == '8'
  assert last_letter('funnyguys') == 's'
  assert last_letter('101') == '1'
  print("YOUR CODE IS CORRECT!")
test_last_letter()

#Task 5
def string_length(word):
    return len(word)
def test_string_length():
  assert string_length('hello!') == 6
  assert string_length('banana') == 6
  assert string_length('8') == 1
  assert string_length('funnyguys') == 9
  assert string_length('101') == 3
  print("YOUR CODE IS CORRECT!")
test_string_length()

#Task 6
def bigger_guy(age, age1):
    if age < age1:
        return age1
    else:
        return age
    return
def test_bigger_guy():
  assert bigger_guy(1, 2) == 2
  assert bigger_guy(10, 20) == 20
  assert bigger_guy(20, 10) == 20
  assert bigger_guy(10, 10) == 10
  assert bigger_guy(2, 1) == 2
  assert bigger_guy('a', 'b') == 'b' # 'b' is greater than 'a'
  print("YOUR CODE IS CORRECT!")
test_bigger_guy()

#Task 7
def biggest_guy(age, age1, age2):
    arr =[]
    arr.append(age)
    arr.append(age1)
    arr.append(age2)
    return max(arr)
def test_biggest_guy():
  try:
    assert biggest_guy(1, 3, 2) == 3
    assert biggest_guy(30, 10, 20) == 30
    assert biggest_guy(20, 10, 30) == 30
    assert biggest_guy(2, 1, 9) == 9
    assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'

  except (AssertionError) as e:
    print(e)
    print("Wrong!!")

  print("Correct buddy!!!")
test_biggest_guy()

#Task 8


def number_to_choice(number):
    dict_12 ={
        1:'Usain',
        2:'Me',
        3:'Aybek'
    }
    return dict_12.get(number)

def test_number_to_choice():
   assert number_to_choice(1) == 'Usain'
   assert number_to_choice(2) == 'Me'
   assert number_to_choice(3) == 'Aybek'
   print("YOUR CODE IS CORRECT!")

print (test_number_to_choice())


#slide1

def reverse_list(list_):
    arr = []
    s = int(len(list_)/2)
    list_.reverse()
    arr = list_[s:]
    for i in list_[:s]:
        arr.append(i)
    print(arr)
reverse_list(['name', 'age', '1', '19'])

#slide2

def fibonachi():
    fib1 = fib2 = 1
    print(fib1, fib2 , end= ' ')
    for i in range(2,10):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2 , end=' ')
fibonachi()

#slide3

def slojenie(a,b):
    return a+b

def vyzitanie(a,b):
    return a-b

def summ():
    print('\n',slojenie(1,2))
    print(vyzitanie(1,2))
summ()

#slide4
def crate_file(name):
    with open(f'{name}.txt', 'w') as file:
        file.write('a')
file_ = crate_file('aman')

#slide5
from random import choice

def gen_number():
    number_choice = ['1','4','5','7','9','0']
    number = '0444'
    for i in range(0,6):
        number += choice(number_choice)
    print(number)

gen_number()
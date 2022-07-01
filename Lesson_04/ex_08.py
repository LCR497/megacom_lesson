k = int(input('Сколько можно положить на сквовроду -- '))
m = int(input('Обжарка с одной стороны -- '))
n = int(input('Количество котлет -- '))
if n<=k:
    t = 2*m
elif n*2 % k ==0:
    t = m*(n*2 // k)
else:
    t = m*(1+(n*2//k))
print(t)

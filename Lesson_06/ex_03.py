import random
m = 0
n = 1000
for i in range(n):
    if i % 2 == 0:
        m+=1
result = (m/1000)*100
print(result)
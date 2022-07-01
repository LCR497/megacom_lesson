months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
month = months_a.union(months_b)
print(month)
month.add('Dec')
print(month)
for i in month:
    print(i)
x = {1, 2, 3}
y = {4, 3, 6}
c = set()
c =x.intersection(y)
print(c)
x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
if x1 > 0 and y1 > 0:
    if x2 > 0 and y2 > 0:
        print('Yes')
    else:
        print('No')
elif x1 < 0 and y1 > 0:
    if x2 < 0 and y2 > 0:
        print('Yes')
    else:
        print('No')
elif x1 < 0 and y1 < 0:
    if  x2 < 0 and y2 < 0:
         print('Yes')
    else:
         print('No')
else:
   if x2>0 and y2<0:
       print('Yes')
   else:
       print('No')

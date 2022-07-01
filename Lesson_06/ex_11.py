# 1
# *
# **
# ***
# ****
# *****
#
# 2
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
#
#
# 3
draw = '''        
        *
       **
      ****
    ******
  ********
 **********
  ********
    ******
     ****
      **
       *'''

print('First Draw')
for i in range(1,6):
    print('*'*i)


print('Second Draw')
n = 0
while n <= 9:
    if n < 5:
        for i in range(1,6):
            print('*' * i)
            n+=1
    else:
        for j in range(6,0,-1):
            print('*' * j)
            n+=1

print('Third Draw')
print(draw)
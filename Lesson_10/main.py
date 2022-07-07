#Problem1
er_list = [15,24,81,132,196,214]
list_or = [i for i in range(1,255) if i not in er_list]
print(list_or)
#Problem2
N = 6
M = 6
A = [ [0]*M for i in range(N) ]
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])
print(A[5])
#Problem3
k = 0
login_list =[]
pass_list = []
while k<=2:
    login = input('Login ')
    login_list.append(login)
    password = input('Password ')
    pass_list.append(password)
    k+=1
dictt = {i:j for i in login_list for j in pass_list }
print(dictt)
#Problem4
names = ['Kairat', 'Erlan', 'Dastan', 'Artur', 'Bahtoolot', 'Azat', 'Bakyt']
print(sorted(names))

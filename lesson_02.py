k = int(input('Sum of credit: '))
p = int(input('Your rate of interest: '))
m = int(input('Month: '))
print(k*0.01*p*(1+0.01*p)**m/((1+0.01*p)**m-1))


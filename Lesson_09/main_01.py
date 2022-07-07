user = input('Login: ')
password = input('Password: ')
with open('user.txt', 'w') as f:
	f.write(f'{user} {password}')


with open('user.txt', 'r') as file:
	if 'w' in file.read():
		print('Yes w')
	else:
		print('No w')

t_words = []
with open('database.txt', 'a') as f:
	while True:
		login = input('Login:  ')
		password = input('Password: ')
		t_words = f.read()

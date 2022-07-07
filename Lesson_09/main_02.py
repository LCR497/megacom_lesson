t_words = []
with open('python.txt', 'r') as file:
	slova = file.read().lower().split(' ')
	print(slova)
	for i in slova:
		if 't' in i:
			t_words.append(i)
print(t_words)

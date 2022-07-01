city = []
paginator = 0
status = True
menu = '''1. Добавить новый город
2. Отобразить список городов
3. Заменить город
4. Удалить город
5. Выход'''
while status:
	print(menu)
	choose = int(input('Выберите действие --> '))
	if choose == 1:
		city_name = input('Введите название города: ')
		if city_name in city:
			print(f'Такой город уже есть! {city_name}')
		else:
			city.append(city_name)
			print('Город добавлен!')
	if choose == 2:
		for i in city:
			paginator+=1 
			print(paginator,i)
			paginator = 0
	if choose == 3:
		name_old = input('Текущий город: ')
		name_new = input('Новый город: ')
		if name_old in city:
			for i in range(len(city)):
				if city[i] == name_old:
					city[i] = name_new
					print('Город заменен')
				else:
					print('Некорректное название!')
		else:
			print('Текущий город отсутствует')
	if choose == 4:
		name_delete = input('Введите название города: ')
		if name_delete in city:
			for i in range(len(city)):
				if city[i] == name_delete:
					del city[i]
					print('Город удален!')
				else:
					print('Некорректное название!')
		else:
			print('Текущий город отсутствует.')
	if choose == 5:
		break
	

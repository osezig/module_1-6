# работа со словарями
my_dict = {'Sergey': 1981, 'Biba': 1999, 'Boba': 2000}
print(my_dict)
print(my_dict['Sergey'])
print(my_dict.get('Gala', 'Такого ключа не существует'))
my_dict.update({'Anna': 1900, 'Vasiliy': 1911})
print(my_dict)
a = my_dict.pop('Anna')
print(my_dict)
print(a)
print(my_dict)

# работа со множествами
my_set = {1, (2, 3, 4), 'Fara', 8.5}
print(my_set)
my_set.add('gaha')
my_set.add('paha')
print(my_set)
my_set.discard('gaha')
print(my_set)
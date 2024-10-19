# Работа со словарями

my_dict = {'Andrey': 1999, 'Ivan': 2006, 'Roma': 2001, 'Dasha': 1989}
print(my_dict)
print(my_dict['Roma'])
print(my_dict.get('Sasha'))
my_dict.update({'Timur': 2007, 'Ruslan': 2019})
print(my_dict.pop('Andrey'))
print(my_dict)

# Работа с множествами

my_set = {2, 4, 2, 'string', False, False, 2}
print(my_set)
my_set.add(7)
my_set.add('car')
my_set.discard(4)
print(my_set)

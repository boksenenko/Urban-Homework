#1
my_dict = {'Bogdan': 1999, 'Arina': 2002, 'Nikita': 2000}
print(my_dict)
print(my_dict['Bogdan'])
print(my_dict.get('Dasha'))
my_dict['Maxim'] = 1988
my_dict['Artem'] = 1989
a = my_dict.pop('Bogdan')
print(a)
print(my_dict)

#2
my_set ={1, 2, 2, 3, 3, 5, 5, 'Name', 'Name'}
print(my_set)
my_set.update([6, 6, 7, 7, 2, 2])
my_set.discard(2)
print(my_set)
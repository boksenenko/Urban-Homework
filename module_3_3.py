#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 'another string')
print_params('string')

#2
values_list = [2, 'str', False]
values_dict = {'a': 6, 'b': False, 'c': 'str_2'}
print_params(*values_list)
print_params(**values_dict)

#3
values_list_2 = [62, False]
print_params(*values_list_2, 42)
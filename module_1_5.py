#1
immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
#2
#immutable_var[0] = 3
#print(immutable_var)
#3 Изменить данные в кортеже невозможно, это и отличает его от списка. Изменить данные можно только если создать список внутри кортежа.
#4
mutable_list = [1, 2, 3, 'abc', True]
print(mutable_list)
mutable_list[0] = 4
print(mutable_list)


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, 2.5, False]
print_params(*values_list)
values_dict = {'a': 2, 'b': 3, 'c': 4}
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Vasya'])
print('Not existing value:', my_dict.get('Sasha', 'Токого имени нет'))
my_dict.update({'Olga': 2001, 'Gleb': 2014})
name = my_dict.pop('Vasya')
print(my_dict)
print('Deleted value:', name)
print('Modified dictionary:', my_dict)

my_set = {1.157, True, 'Корова', 3, 5}
print('Set:', my_set)
my_set.add(4)
my_set.add(6)
my_set.remove('Корова')
print('Modified set:', my_set)

my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1.0, 2.0, 3.0, 4.0, 5.0],
    'dict': {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять'},
    'set': {'random_1', 'random_2', 'random_3', 'random_4', 'random_5'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(6.0)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'not really'
my_dict['dict'].pop('three')

my_dict['set'].add('random_6')
my_dict['set'].pop()

print(my_dict)

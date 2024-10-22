def calc_operations(result_operations):
    lst = result_operations.split()
    operations = int(lst[-1])
    return operations + 10


str_1 = 'результат операции: 42'
str_2 = 'результат операции: 54'
str_3 = 'результат работы программы: 209'
str_4 = 'результат: 2'

print(calc_operations(str_1))
print(calc_operations(str_2))
print(calc_operations(str_3))
print(calc_operations(str_4))

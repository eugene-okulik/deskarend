string_1 = 'результат операции: 42'
string_2 = 'результат операции: 514'
string_3 = 'результат работы программы: 9'

num_1 = int(string_1[string_1.index(': ') + 1:]) + 10
num_2 = int(string_2[string_2.index(': ') + 1:]) + 10
num_3 = int(string_3[string_3.index(': ') + 1:]) + 10

print(num_1, num_2, num_3)

def what_is_a_num():
    exp_num = 5
    while True:
        num = int(input('Enter a number '))
        if num == exp_num:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('попробуйте снова')
            continue

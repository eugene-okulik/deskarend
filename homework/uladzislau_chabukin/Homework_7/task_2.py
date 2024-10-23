def special_print_dict(dictionary):
    for key, value in dictionary.items():
        print(f'{key * value}')


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
special_print_dict(words)

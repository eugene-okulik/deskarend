text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
additive = 'ing'

result_lst = []
for word in text.split():
    if word.endswith('.') or word.endswith(','):
        result_lst.append(word[:-1] + additive + word[-1])
    else:
        result_lst.append(word + additive)
print(' '.join(result_lst))

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path', help='Directory path')
parser.add_argument('-t', '--text', help='Text for search')
args = parser.parse_args()

search_word = args.text
directory_path = args.path

files = os.listdir(directory_path)

for file in files:
    file_path = os.path.join(directory_path, file)

    with open(file_path) as file_data:
        lines = file_data.readlines()

    for line_number, line in enumerate(lines, start=1):
        if search_word in line:
            words_in_line = line.split()

            search_word_indexes = [i for i, word in enumerate(words_in_line) if search_word in word]

            print(search_word_indexes)
            for index in search_word_indexes:
                first_five_words_index = 0 if index <= 5 else (index - 5)
                first_five_words = ' '.join(words_in_line[first_five_words_index:index])
                last_five_words_index = -1 if (len(words_in_line) - index <= 5) else (index + 5 + 1)
                last_five_words = ' '.join(words_in_line[index + 1:last_five_words_index])

                print(f'Файл: {file}, номер строки: {line_number}', end=' ')
                print('Результаты поиска:', first_five_words, words_in_line[index], last_five_words)

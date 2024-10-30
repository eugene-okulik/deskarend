import datetime
import os

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


for line in read_file():
    now = datetime.datetime.now()
    date = line[line.find(' ') + 1: line.find(' -')]
    python_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    if line[0] == '1':
        print(python_date + datetime.timedelta(days=7))
    elif line[0] == "2":
        print(python_date.weekday())
        # Так понятней
        # print(datetime.datetime.strftime(python_date, '%A'))
    elif line[0] == "3":
        print((now - python_date).days)

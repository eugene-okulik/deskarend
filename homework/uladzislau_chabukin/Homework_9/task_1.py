import datetime

data = "Jan 15, 2023 - 12:05:33"

python_data = datetime.datetime.strptime(data, '%b %d, %Y - %H:%M:%S')
print(python_data.strftime('%B'))
print(python_data.strftime('%d.%m.%Y, %H:%M'))

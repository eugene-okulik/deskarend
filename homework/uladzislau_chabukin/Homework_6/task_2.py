for i in range(1, 100 + 1):
    if i % 15 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# Или

for i in range(1, 100 + 1):
    if i % 3 == 0:
        if i % 5 == 0:
            print('FuzzBuzz')
        else:
            print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

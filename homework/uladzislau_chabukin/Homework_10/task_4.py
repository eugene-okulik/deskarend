PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

PRICES = PRICE_LIST.split()
PRICE_DICT = {PRICES[i]: int(PRICES[i + 1][:-1]) for i in range(0, len(PRICES) - 1, 2)}
print(PRICE_DICT)

PRICES = PRICE_LIST.split('\n')
BOOKS = [el.split()[0] for el in PRICES]
PRICE = [int(el.split()[1][:-1]) for el in PRICES]
PRICE_DICT = dict(zip(BOOKS, PRICE))
print(PRICE_DICT)

PRICES = PRICE_LIST.split('\n')
PRICE_DICT = {i[0]: int(i[1][:-1]) for i in [j.split() for j in PRICES]}  # СЛОЖНО
print(PRICE_DICT)

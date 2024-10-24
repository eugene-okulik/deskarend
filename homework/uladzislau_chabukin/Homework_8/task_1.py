import random


def get_bonus_salary(salary):
    bonus = random.choice((True, False))
    if bonus:
        bonus_salary = int(salary * (1 + random.random()))
        return f'${bonus_salary}'
    return f'${salary}'

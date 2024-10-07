def main():
    znak = input('Выберите знак операции(+, -, *, /): ')
    chislo1 = float(input('a = '))
    chislo2 = float(input('b = '))
    print(calc(znak, chislo1, chislo2))

def calc(znak, chislo1, chislo2):
    if znak == '+':
        return chislo1 + chislo2
    if znak == '-':
        return chislo1 - chislo2
    if znak == '*':
        return chislo1 * chislo2
    if znak == '/':
        if chislo2 != 0:
            return chislo1 / chislo2
        return 'Деление на ноль!'

    return 'Неверный знак операции!'

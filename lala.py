from math import sqrt


message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Num):
    """Вычисляет квадратный корень"""
    return sqrt(Num)


def calc(your_number):
    if your_number <= 0:
        return

    print(f'Мы вычислили квадратный корень из введённого Вами числа.'
           'Это будет: {your_number}')


print(message)
calc(25.5)

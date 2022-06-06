# 3,1415926535897932384626433832795

def Calculate_pi (accuracy):
    d = 10 ** -accuracy
    pi = 3
    significant = 4
    value = 1
    while d < abs(value):
        value = 4 / significant / (significant - 1) / (significant - 2)
        if significant % 4 != 0:
            value *= -1
        pi += value
        significant += 2
    return round(pi, accuracy)

accuracy = int(input('Введите количество значащих цифр после запятой, которые нужно определить в числе пи: '))
pi = Calculate_pi(accuracy)
print(f'Число пи с точностью до {accuracy}-го знака равно {pi}')
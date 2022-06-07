from itertools import count


def Prime_factors (num):
    res = []
    count = 2
    while count * count <= num:
        if num % count == 0:
            res.append(count)
            num //= count
        else:
            count += 1
    if num > 1:
        res.append(num)
    primes = set(res)
    return primes

number = int(input('Введите натуральное число: '))
res = Prime_factors(number)
print(res)
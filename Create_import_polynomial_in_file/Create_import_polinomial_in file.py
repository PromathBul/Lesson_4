from random import randint

def Create_list_natural_numbers (length, max):
    nat_nums = []
    for i in range (length):
        nat_nums.append(randint(0, max))
    return nat_nums

power = randint(1, 5)
max_coeff = 100
coeffs = Create_list_natural_numbers(power + 1, max_coeff)
print(coeffs)
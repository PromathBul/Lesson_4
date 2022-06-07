from random import randint

def Create_list_natural_numbers (length, max):
    nat_nums = []
    for i in range (length):
        nat_nums.append(randint(0, max))
    return nat_nums

def Print_power_equation (coeffs):
    equation = ''
    for i in range (len(coeffs) - 1, 0, -1):
        if coeffs[i] != 0:
            if i == 1:
                equation += f'{coeffs[i]}x + '
            else:
                equation += f'{coeffs[i]}x^{i} + '
    if coeffs[i] == 0:
        equation += ' = 0'
    else:
        equation += f'{coeffs[0]} = 0'
    return equation

power = randint(1, 5)
max_coeff = 100
coeffs = Create_list_natural_numbers(power + 1, max_coeff)
print(coeffs)
first_equation = Print_power_equation(coeffs)
print(first_equation)

first_file = 'First_power_equation.txt'
with open(first_file, 'w') as data:
    data.writelines(first_equation)

power = randint(1, 5)
coeffs = Create_list_natural_numbers(power + 1, max_coeff)
print(coeffs)
second_equation = Print_power_equation(coeffs)
print(second_equation)

second_file = 'Second_power_equation.txt'
with open(second_file, 'w') as data:
    data.writelines(second_equation)
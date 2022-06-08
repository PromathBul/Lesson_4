import Print_power_equation as Print

def Get_coeffs (equation):
    coeffs = []
    equation = ' ' + equation

    if first_equation[-6] != ' ':
        coeffs.append(int(f'{equation[-6]}{equation[-5]}'))
    elif equation[-5] != ' ':
        coeffs.append(int(equation[-5]))
    else:
        coeffs.append(0)

    ind = equation.find('x ')
    if ind == -1:
        coeffs.append(0)
    else:
        coeffs.append(int(f'{equation[ind -2]}{equation[ind - 1]}')) if equation[ind - 2] != ' ' \
            else coeffs.append(int(equation[ind - 1]))

    terms = equation.count('+')
    for i in range (2, terms + 1):
        ind = equation.find(f'x^{i}')
        if ind == -1:
            coeffs.append(0)
        else:
            coeffs.append(int(f'{equation[ind -2]}{equation[ind - 1]}')) if equation[ind - 2] != ' ' \
                else coeffs.append(int(equation[ind - 1]))
    return coeffs

def Sum_equations(coeffs_first, coeffs_second):
    if len(coeffs_first) >= len(coeffs_second):
        min_lst = coeffs_second
        max_lst = coeffs_first
    else:
        min_lst = coeffs_first
        max_lst = coeffs_second

    coeffs_sum = max_lst.copy()
    for i in range(len(min_lst)):
        coeffs_sum[i] = coeffs_sum[i] + min_lst[i]
    return coeffs_sum

path = 'Lesson_4\Create_import_polynomial_in_file\First_power_equation.txt'
first_equation = ''
with open(path, 'r') as data:
    first_equation = data.read()
print(f'Первое уравнение:\n{first_equation}')

path = 'Lesson_4\Create_import_polynomial_in_file\Second_power_equation.txt'
second_equation = ''
with open(path, 'r') as data:
    second_equation = data.read()
print(f'Второе уравнение:\n{second_equation}')

coeffs_first = Get_coeffs(first_equation)

coeffs_second = Get_coeffs(second_equation)

coeffs_sum = Sum_equations(coeffs_second, coeffs_first)

sum_equation = Print.Print_power_equation(coeffs_sum)
print(f'Суммарное уравнение:\n{sum_equation}')

my_file = 'Lesson_4\Export_from_files_and_sum_power_equations\Sum_equation.txt'
with open(my_file, 'w') as data:
    data.writelines(sum_equation)
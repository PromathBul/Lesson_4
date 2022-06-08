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
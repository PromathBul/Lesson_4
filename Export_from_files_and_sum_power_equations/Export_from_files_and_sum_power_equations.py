path = 'First_power_equation.txt'
first_equation = ''
with open(path, 'r') as data:
    first_equation = data.read()
print(f'Первое уравнение:\n{first_equation}')

path = 'Second_power_equation.txt'
second_equation = ''
with open(path, 'r') as data:
    second_equation = data.read()
print(f'Второе уравнение:\n{second_equation}')

print(terms_first = first_eqaution.count('+'))

#for i in range ()
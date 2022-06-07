from ast import Mult
import Create_list_random_nums_from_0_to_9 as create

length = int(input('Введите количество чисел в изначальной последовательности: '))
my_list = create.Create_list_random_int_from_0_to_9(length)
print(f'Изначальная последовательность:\n{my_list}')

my_list = list(set(my_list))
print(f'Список неповторяющихся элементов изначальной последовательности:\n{my_list}')
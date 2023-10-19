"""
import sys
sys.path.append('C:/Users/uhnov/OneDrive/Рабочий стол/УЧЕБА GB/PYTHON/Collection')
import func as f
"""

def input_number(text) -> int:
    print(text, end='')
    while True:
        try:
            number = int(input())
        except ValueError:
            print('Pls input a number (int): ', end='')
            continue
        else:
            break
    return number

def gener_list_rnd_randint(begin_num, end_num, len_list):
    import random
    return [random.randint(begin_num, end_num) for _ in range(len_list)]

def gener_list_input_int_only(text):
    length = input_number(text)
    return [value := input_number(f'{_ + 1} value is: ') for _ in range(length)]

def gener_list_rnd_randiant_unique(begin_num, end_num, len_list):
    import random
    list = gener_list_rnd_randint(begin_num, end_num, len_list)
    for i in range(1, len(list)):
        while list[i] in list[:i]:
            list[i] = random.randint(begin_num, end_num)
    return list



# функция, которая принимает два списка 
# возвращает True, если у них есть хотя бы один общий член.
def equal_value_list(list_1, list_2):
    count = 0
    for value in list_2:
        if value in list_1:
            count += 1
    return True if count > 0 else False

def equal_value_list_t_set(list_1, list_2):
    return False if not set(list_1).intersection(set(list_2)) else True

# функция, чтобы перемешать (в случайном порядке) и распечатать указанный список.


# быстрая сортировка списка


from random import randint

def Create_list_random_int_from_0_to_9 (length):
    random_list = []
    for item in range(length):
        random_list.append(randint(0, 9))
    return random_list
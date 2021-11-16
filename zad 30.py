import random
def rand_elem(array):
    return array[random.randint(0, len(array)-1)]
print(rand_elem([4,6,24,21,7,0,54,3]))
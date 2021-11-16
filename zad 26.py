array = [1,2,3,4,5,6,7,8,9]
is_odd = lambda x: x % 2 != 0
print(sorted(array, key=is_odd))
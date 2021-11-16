arr = [2, 3, 2, 5, 8, 1, 9, 8]
uniques = []
for i in arr:
    if i not in uniques:
        uniques.append(i)
print(uniques)
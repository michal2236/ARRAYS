def is_subset(arr1, arr2):
    subset_count = 0
    for el in arr1:
        if el in arr2:
            subset_count += 1
    return subset_count == len(arr1)

print(is_subset([1,2,6], [1,5,3,2,6,3]))
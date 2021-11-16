def bubble_sort(array):
    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[j-1] > array[j]:
                [array[j-1], array[j]] = [array[j], array[j-1]]
    return array

print(bubble_sort([43,12,54,23,3]))
print(bubble_sort([-5,4,2,42,1]))
print(bubble_sort([5,32,5,-4,21,-6,0]))
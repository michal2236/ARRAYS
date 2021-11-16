number = int(input("Number: "))
array = [1,22,4,4,43,6,43,8,12,10]
for i in range(0, len(array)):
    if(i > number):
        print(array[i], end=" ")
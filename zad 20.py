def occurs(number, array):
    if number in array:
        print(f"number {number} appers in the array {array}")
    else:
        print(f"number {number} not appers in the array {array}")
occurs(23, [15, 38, 7, 23, 14])
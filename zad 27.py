def separatedByCommas(array):
    string = ""
    for i in array:
        string += f"{i}, "
    return string
print(separatedByCommas([5,4,3,2,6,5]))
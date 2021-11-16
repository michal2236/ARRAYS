array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_index = ""
chars = 0

for i in range(0, len(array)):
    if(len(array[i]) > chars):
        chars = len(array[i])
        longest_index = i
print(array[longest_index])
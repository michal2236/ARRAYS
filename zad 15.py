colors = ["red", "green", "blue", "yellow"]


file = open('colors.txt', 'a')
for color in colors:
    file.write(color + "\n")
file.close()
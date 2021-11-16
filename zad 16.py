array = [12, 6, 4, 9, 3]

def stars(n):
    print(f"{n}:", end=" ")
    for i in range(0, n):
        print("*", end="")
    print()
    
for i in array:
    stars(i)
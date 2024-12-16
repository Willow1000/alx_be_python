pattern_size = int(input("Enter the size of the pattern: "))

while pattern_size:
    for i in range(pattern_size.copy()):
        print("*",end="")
    pattern_size-=1    
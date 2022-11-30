key = int(input("Enter a number: "))
for item in range(key+1):
    for elem in range(1, item+1):
        print(elem, end="")
    print()

key =int(input("Enter a number: "))
item = -1
for elem in range(key):
    item += 1
    numb = elem*elem*elem

    print(f"number is :{item} and cube of the {item} is :{numb}")

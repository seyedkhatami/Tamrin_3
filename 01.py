num = input("Enter a num: ").split()
a = 0
b = 0
for items in num:
    b += int(items)
    a += 1
average = b//a
print(f"sum => {b} . average => {average}")


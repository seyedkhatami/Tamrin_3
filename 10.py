key = int(input("Enter a number: "))
while key > 9:
    s = 0 
    while key != 0:
        b = key % 10 
        key = key //10
        s += b
    key = s 
    print (key)

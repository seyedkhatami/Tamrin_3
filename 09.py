key1 = int(input("Enter a number :"))
key2 = int(input("Enter a number :"))

big = key1 
small = key2
if key1 < key2:
    big = key2
    small = key1
while small != 0:
    c = big % small
    big = small
    small = c 
    print(f"Greatest common denominator: {big}")
    print (f"The Lowest common denominator: {(key1*key2)//big}")  

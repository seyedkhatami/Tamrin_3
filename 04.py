key = 0
tike = chr(10347)
while key <100:
    key += 1
    if key % 2!=0:
        print (f"Odd number: {key}")
    elif key % 3 == 0 and key % 15 != 0:
        print(f"Odd number: {key} => 3 {tike} and => 15 X ")

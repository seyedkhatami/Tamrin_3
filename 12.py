key = int(input("Enter a number :"))
num = key 
data = 0
while key!= 0:
    b = key%10
    key = key//10
    data = ((data * 10)+b)
if num == data:
    print ("True")
else :
    print("False")

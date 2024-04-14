# Obtain a positive integer from the user
positive_integer=int(input("Please input any positive number: "))
total=0

# for loop,
for i in range(1,positive_integer+1):
    total+=i
    print(i,end=" ")
    if i == positive_integer :
        print(end=" ")
    else:
       print(" + ",end="")
print("=",total)

if positive_integer < 0 :
    message="Enter 'z' to exit"
    while positive_integer !='z' :
        positive_integer=input(message)

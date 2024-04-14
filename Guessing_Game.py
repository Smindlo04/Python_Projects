import time
import random
value = random.randint(1,5)
store = []
count = 1
stop = time.time()
now2 = time.gmtime()
now3 = time.asctime(now2)

while count!= 0:
    start = time.time()
    now = time.gmtime()
    now = time.asctime(now)
    user = int(input("Please enter a number: "))
    if user == value:
        print("Correct guess")
        store.append(user)
        counter = 0
        for i in store:
            counter += 1
        print("it took you",counter,"times To get it right",round(start-stop,2),"seconds")



    elif user != value:
        store.append(user)
        counter = 0
        for i in store:
            counter += 1
        print("opps incorrect guess")
        check = int(input("press 1 to continue or zero to quit: "))
        if check == 0:
            count = count - 1

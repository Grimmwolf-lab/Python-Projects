import random
from time import sleep

dice = [1,2,3,4,5,6]

print("Press 1.To roll the dice 2. To exit")
c = int(input("Please enter a choice:"))
if c==1:
    print("Rolling the dice......")
    sleep(3)
    print(random.choice(dice))
    ans = input("Do you want to roll again?")
    while ans =="yes" or ans =="y":
        print("Rolling the dice......")
        sleep(3)
        print(random.choice(dice))
        break
else:
    print("Thank you for playing with us!")

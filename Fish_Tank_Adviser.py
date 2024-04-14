# image of the fish
print('''
            ooo
       o            o
    o                  o      o
  o                      o   o
o       o                 o o
  o                      o   o
    o                  o      o
       o            o
             oo
                                 ''')

print("INORDER TO STOP THE LOOP PRESS CONTROL+C")

# Obtain information from the user
name=input("Please provide me with your name: ")
r=float(input("Please input the radius of the fish tank in centremetres: "))
h=float(input("Please input the height of the fish tank in centremetres: "))

# greetings to the user
print("Hi",name,"I will provide you with the amount of water needed to fill your fish tank. ")

#math import
import math
import random

#calculations required
volume=math.pi*r**2*h
print("The shape of the tank is a cylinder")
print("The volume of the fish tank is: ",int(volume),"ml")
print("The amount of water a tank can hold: ",round(volume/1000,1),"L")
print("The volume of water one tiny fish would need: ",1.5*1000,"ml")
print(round(volume/1000*0.67),0, "fish can be accomodated by your tank")

#information about feeding the fish
print('''\n Did you know?
           Feed your fish twice a day.
           DO NOT overfeed, as this may :
           1. cause indigestion, and
           2. contaminate your fish tank.
           A good rule of thumb is to only feed
           an amount that the fish can consume
           in less than two minutes.
        ''')

#while loop,
discount=0

while discount>=0 and discount<=10 :
    discount=random.randint(0,10)
    print(discount)

import random
import time as t
print("Welcome to Dice Rolling")
min=1
max=6
roll_the_dice=input("Type Yes To Roll\n")
if roll_the_dice=='Yes':
	print("Rolling the dice")
	t.sleep(3)
	print("The Lucky value is")
	number_arrived=random.randint(min,max)
	print(number_arrived)
else :
   print("Thanks for Trying your Luck")



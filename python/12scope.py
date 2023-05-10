# guess the number
import random

target = random.randrange(100)
print(target)

level = input("Enter the level. Type 'easy' or 'hard' : ")
chances = 0
if(level == 'easy'):
    chances = 10
else:
    chances = 5

while(chances):
    print(f"You have {chances} chances to guess the number")
    x = int(input("Make a guess : "))
    if(x == target):
        print("You guessed it right. You Win!!")
        break
    elif(x > target):
        print("Too high")
    else:
        print("Too low")

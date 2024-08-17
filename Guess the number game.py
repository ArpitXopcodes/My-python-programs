'''guess the number game'''

import random
computer = random.randint(1,100)
a = -1 #doubt
guesses = 0 #doubt
while(a != computer):
    guesses +=1 #doubt
    a=int(input("enter your number :"))
    if(a>computer):
       print("lower number please")
    else:
        print("higher number please")

print("congrats you have guessed the number")

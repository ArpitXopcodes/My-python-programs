'''
rock=-1
paper=0
scissor=1

'''
import random

youdict={"rock":-1,"paper":0,"scissor":1}

computer= random.choice([-1,0,1])

youstr=(input("enter your move :"))

reversedict={-1:"rock",0:"paper",1:"scissor"}

if youstr in youdict:
    you=youdict[youstr]
    
print(f"you choose {reversedict[you]} \n computer choose {reversedict[computer]} ")


if(computer==you):
    print("its a draw")

elif(computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
    print("you lose")

else:
    print("you win")

'''high score tracer in python'''


import random

def game():
    return random.choice([1,2,3,4,5,6,7,8,9,10])
new=game()

with open("high score.txt","r+") as f:
    a=f.read().strip()
'''remeber u should have a file called high score.txt in your computer'''
if a:
     a=int(a)
else:
     a=0

if new > a:
    print("new high score")
    with open("high score.txt","w") as f:
        f.write(str(new))
else:
        print("try again later")

game()

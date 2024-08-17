'''bank withrawl debit and credit'''

class account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc

    def debit(self,amt):
        self.bal -= amt
        print(f"rs {amt} is debited")
        print("balence remaining is", self.new_bal())


    def credit(self,amt):
        self.bal += amt
        print(f"rs {amt} is credited")
        print("balence remaining is", self.new_bal()) 

    def new_bal(self):
        return self.bal
    

ac1=account(100000,12345)
print(ac1.bal,ac1.acc)
ac1.debit(1000)
ac1.credit(500)

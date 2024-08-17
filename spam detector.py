'''spam detector'''
p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this" 

comment=(input("enter your comment :"))


if (p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment):
    print("this is a spam comment please ignore this comment")

else:
    print("read this comment its not spam")

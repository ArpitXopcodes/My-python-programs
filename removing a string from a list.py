'''removing a string from a list'''

def rem(l, a):
    if a in l:
        l.remove(a)
    return l

a = input("Enter the name you want to remove from the list: ")

l = ["akhil", "arpit", "shourya", "ridheman", "noob"]

print(rem(l, a))

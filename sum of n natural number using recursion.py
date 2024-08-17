'''sum of n natural numbers using recursion'''

def sum(i):
    if i == 1:
        return 1
    return i + sum(i-1)

i = int(input("The number which you want to sum up to: "))

print(f"The sum of all the numbers between 1 to {i} is {sum(i)}")


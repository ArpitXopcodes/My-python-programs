'''average of 3 numbers with func'''

def avg():
    a= int(input("enter your number : "))
    b= int(input("enter your number : "))
    c= int(input("enter your number : "))
    average = (a+b+c)/3
    print(average)
    return "average"

a=avg() #funct call
print(a)

n=input("enter your name: ")
def greet():
    print(f"good day to you {n}")
    return "<3" '''argument returned when i 
    called the fuction and gave it 
    a variable and printed that variable'''

b=greet()#func call
print(b)    

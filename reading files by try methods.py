'''reading files in python'''
#make sure to have all the files in txt form before u open them with open("")

try:

   with open("1.txt") as f:
    print(f.read())

except Exception as e:
    print(e)
    print("invalid input")
 
try:
   with open("2.txt") as f:
    print(f.read())
except Exception as e:
    print(e)
    print("invalid input")
try:

   with open("3.txt") as f:
    print(f.read())
except Exception as e:
    print(e)
    print("invalid input")


'''accessing and editing files in python '''

#remeber to have a file name noob.txt in your system and it may contain arpit in it to replace with str
with open("noob.txt","r") as f:
    a = f.read().strip()

str = "ridheman"

if "arpit" in a:
    print(f"Replacing the word 'arpit' with '{str}'")
    a = a.replace("arpit", str)
    with open("noob.txt", "w") as f:
        f.write(a)
else:
    print("arpit not found")

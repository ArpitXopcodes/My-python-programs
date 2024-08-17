'''utilizing other files 
in my computer
for programming'''

f=open("chap 1.py")
data=f.read()
print(data)
f.close()

str="akhil is noob"
h=open("noob.txt","w")
data=h.write(str)
h.close()



g=open("noob.txt")
line=g.readline()
print(line,type(line))
g.close()

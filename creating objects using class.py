'''Creating Objects'''

class employes:
    def __init__(self,name,salary,language,height):
        self.name=name
        self.salary=salary
        self.language=language
        self.height=height

arpit=employes("arpit",123000,"c++,python","6ft")
print(arpit.height,arpit.language,arpit.name,arpit.salary)
print()#for a new line 

nidhi=employes("nidhi",1400000,"java,html","5.8ft")
print(nidhi.name,nidhi.height,nidhi.language,nidhi.salary)
print()#for a new line 

sharda=employes("sharda",1500000,"none","5.2ft")
print(sharda.name,sharda.height,sharda.language,sharda.salary)
print()#for a new line 

swapnil=employes("swapnil",1600000,"c,csharp","6ft")
print(swapnil.name,swapnil.height,swapnil.language,swapnil.salary)
print()#for a new line 

'''constructors in classes for not giving argument'''

class employee:

    language="py"
    salary=1200000
    #this self in every function passes a argument in the class which is used set up your own value
    
    def __init__(self,name,salary,language):#dunder method is the methodwhich calls itself without anyone calling and it alse had underscores which represents dunder methods
        self.name=name
        self.salary=salary
        self.language =language

        print("i am creating a object")

    def getinfo(self):
        print(f"the language is {self.language} .the salary is {self.salary}")

@staticmethod
def greet():
    print("good morining")

arpit=employee("arpit",140000,"rust")

print(arpit.name,arpit.salary,arpit.language)

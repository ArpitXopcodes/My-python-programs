'''parent class in python with eg'''

class employee:
    company="ITC"
    def show(self):
        print(f"The company id {self.company} and the company is {self.company}")


class programmer(employee):
    company="ITC infotech"
    def show(self):
        print(f"the company is {self.company} and the company is{self.company}")

    def showlanguage(self):
        print(f"the company is {self.company}andhe is good in {self.language}: language")

a=employee()
b=employee()

print(a.company,b.company)

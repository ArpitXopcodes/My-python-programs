'''super methods in python'''

class car:
    def __init__(self,name,type):
        self.type=type
        self.name=name

    @staticmethod
    def start():
            print("car is starting")

    @staticmethod
    def stop():
        print("car is stopped")

class BMwcar(car):
     def __init__(self,name,type):
          super().__init__(type,name)
          
      


car1=BMwcar("m5","motorsport")
print("")
print("type of car 1 is")
print(car1.type)
print(car1.name)

car2=BMwcar("m3","sport")
print("")
print("type of car 2 is")
print(car2.type)
print(car2.name)    

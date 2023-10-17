class person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun(self):
        print(f"My name is {self.name}. \nAge is {self.age}")
class person2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun(self):
        print(f"\nMy name is {self.name}. \nAge is {self.age}")
a=person1("kiran",21)
b=person2("karthi",22)

for x in (a,b):
    x.fun()
   

class cls:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sell(self):
        print(f"My name is {self.name}. \nAge is {self.age}.")
a=cls("Anbu",21)
a.sell()

#change the name
a.name='Bakya'
a.age=20
a.sell()

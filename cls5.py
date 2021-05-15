class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Parent class constructor",name,age)

class Child(Parent):
    def __init__(self,id,name,age):
        super().__init__(name,age)
        self.id=id

    def display(self):
        print(self.id,self.name,self.age)

c1=Child(1,'amit',29)
c1.display()
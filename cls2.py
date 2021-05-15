class Parent:
    def __init__(self):
        print("parent class constructor")
    def show(self):
        print('parent class method')

class Child(Parent):
    def display(self):
        print("child class method")

c1=Child()
c1.display()
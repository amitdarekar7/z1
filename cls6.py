class Parent:
    def __init__(self):
        print("parent class constructor")

    def display(self):
        print("parent class method")

class Child(Parent):
    def __init__(self):
        print("Child class constructor")
    def show(self):
        super().display()
        print("child class method")

c1=Child()
c1.show()
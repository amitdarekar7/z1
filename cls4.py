class Parent:
    def __init__(self):
        print("parent class constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class constructor")
    def show(self):
        print("child class method")

c1=Child()
c1.show()
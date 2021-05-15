class Student:
    branch='mechanical'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def show(m,n):
        print(m,n)

    def detail(self,roll):
        self.roll=roll
        print(roll,self.name,self.age)

    @classmethod
    def display(cls,a):
        cls.a=a
        print(a,cls.branch)

s1=Student(name='amit',age=29)
print(Student.branch)
s1.detail(11)
s1.display('riya')
s1.show('neha','kshitija')
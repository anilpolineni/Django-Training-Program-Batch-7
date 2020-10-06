class ClassA:
    a=20
    b=30
    def display():
        return "I am from ClassA"
    def add(x,y):
        return x+y

class ClassB(ClassA):
    d=20
    f=30
    def show():
        return "i am from ClassB"

obj=ClassB
print(obj.show())

class ClassA:
    def fun1():
        return "i am from ClassA"

class ClassB:
    def fun2():
        return "I am from ClassB"

class ClassC(ClassA,ClassB):
    def fun3():
        return "I am from ClassC"

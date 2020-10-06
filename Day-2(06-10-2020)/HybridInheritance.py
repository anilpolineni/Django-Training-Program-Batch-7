class parent:
    def fun1():
        return "i am from function1"

class Child(parent):
    def fun2():
        return "i am from function2"

class Child1(parent):
    def fun3():
        return "i am from function3"

class Child2(Child,Child1):
    def fun4():
        return "i am from function4"

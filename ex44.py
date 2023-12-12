class Parent(object):
    def implicit(self):
        print("parent implicit()")

class child(Parent):
    pass 
dad = Parent() 
son = child()

dad.implicit()
son.implicit()


#override explicity
class Parent(object):
    def override(self):
        print("parent override()")
class Child(Parent):
    def override(self):
        print("child override()")
dad = Parent()
son = Child()

dad.override()
son.override()
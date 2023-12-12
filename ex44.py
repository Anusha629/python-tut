class Parent(object):
    def implicit(self):
        print("parent implicit()")

class child(Parent):
    pass 
dad = Parent() 
son = child()

dad.implicit()
son.implicit()

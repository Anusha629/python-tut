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

#alter before or after 

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()


#all three combined 

class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

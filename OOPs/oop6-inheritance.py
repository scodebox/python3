class Parent:
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(delf):
        print ('Calling parent method')
        
    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("Parent attr : ",Parent.parentAttr)


class Child(Parent):
    def __init__(self):
        print ('Calling child constructor')

    def childMethod(self):
        print ('calling child method')



c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

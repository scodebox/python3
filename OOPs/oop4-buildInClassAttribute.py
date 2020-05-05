class Employee:
    'Employee class'
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total number of employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name:", self.name)
        print ("Salary :", self.salary)



print ('dict : ',Employee.__dict__)
print ('doc : ',Employee.__doc__)
print ('name : ',Employee.__name__)
print ('module : ',Employee.__module__)
print ('base : ',Employee.__bases__)

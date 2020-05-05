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


emp1 = Employee('Suvam Basak',2000)

emp1.age = 20 #add as 'age' attribute
print (hasattr(emp1,'age')) #Returns true if 'age' is present


emp1.age = 21 #Modify 'age' attribute
setattr(emp1,'age',8)
print (getattr(emp1,'age')) #Returns value of 'age' attribute

delattr(emp1,'age')

#del emp1.age #Delete 'age' attribute

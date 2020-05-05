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
emp1.displayCount()
emp2 = Employee('Raj Paul',200)
emp2.displayCount()


print (Employee.empCount)

emp1.displayEmployee()
emp2.displayEmployee()


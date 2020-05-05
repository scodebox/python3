from collections import namedtuple

# Point = namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
#
# dot_product=(pt1.x*pt2.y)+(pt1.y*pt2.y)
# print(dot_product)


# Car = namedtuple('Car','Price Mileage Colour Class')
# xyz = Car( Class = 'Y', Mileage = 30, Price = 100000,  Colour = 'Cyan')
# print (xyz)
# print (xyz.Class)



total_student = int(input())
fields = input().split()
total_marks = 0
for i in range(total_student):
    Student = namedtuple('Student', fields)
    field1, field2, field3, field4 = input().split()
    student = Student(field1, field2, field3, field4)
    total_marks+=int(student.MARKS)
print(total_marks/total_student)
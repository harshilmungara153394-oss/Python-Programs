#Python Program to Demonstrate the Concept of Inner Class
print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
print("Harshil Mungara")
class Outer:
    def __init__(self):
        print(Outer)
    class Inner:
        def __init__(self):
            print("This is Inner Class")
            
            
a1=Outer()
b=a1.Inner()



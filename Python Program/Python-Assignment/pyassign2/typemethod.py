#Python Program to Demonstrate Various Types of Methods
print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
print("Harshil Mungara")
class Demo:
    def instance_method(self):
        print("This is an instance method")
    @classmethod
    def class_method(cls):
        print("This is a class method")
    @staticmethod
    def static_method():
        print("This is a static method")
d = Demo()
d.instance_method()
Demo.class_method()
Demo.static_method()

# Python Program to Demonstrate the Use of Class
print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
print("Harshil Mungara")
class Student:
  
    def display(self,name, enroll):
        self.name = name
        self.enroll = enroll
        print("Name:", self.name)
        print("Enrollment:", self.enroll)
s1 = Student()
s1.display("XYZ",123)

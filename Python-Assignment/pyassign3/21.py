print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
class Animal:
    def sound(self):
        print("Animal makes a sound")
 
class Dog(Animal):
    def sound(self):
        print("Dog barks")
 
obj = Dog()
obj.sound()

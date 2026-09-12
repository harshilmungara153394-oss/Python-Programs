#Python Program to Show Method Overloading and Overriding
print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
print("Harshil Mungara")
#Method Overloading
class Math:
    def add(self, a, b, c=0):
        return a + b + c
m = Math()
print("Add two numbers:", m.add(40, 60))
print("Add three numbers:", m.add(50, 25, 25))
#Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a = Animal()
a.sound()
d = Dog()
d.sound()

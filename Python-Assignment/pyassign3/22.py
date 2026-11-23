print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
class Animal:
    def eat(self):
        print("Animal eats food")
 
class Dog(Animal):
    def bark(self):
        print("Dog barks")
 
d = Dog()
d.eat()
d.bark()

#Python Program to Demonstrate the Use of Methods
print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
print("Harshil Mungara")
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
c = Calculator()
print("Addition:", c.add(10, 20))
print("Subtraction:", c.subtract(10, 20))

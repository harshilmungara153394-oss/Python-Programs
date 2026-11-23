print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
# Single inheritance
class A:
    def show_a(self):
        print("Class A")
 
class B(A):
    def show_b(self):
        print("Class B")
 
# Multiple inheritance
class X:
    def show_x(self):
        print("Class X")
 
class Y:
    def show_y(self):
        print("Class Y")
 
class Z(X, Y):
    pass
 
# Multilevel inheritance
class C(B):
    def show_c(self):
        print("Class C")
 
# Hierarchical inheritance
class D(A):
    pass
 
b = B()
b.show_a()
b.show_b()
 
z = Z()
z.show_x()
z.show_y()
 
c = C()
c.show_a()
c.show_b()
c.show_c()
 
d = D()
d.show_a()

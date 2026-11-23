print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except (ValueError, ZeroDivisionError) as error:
    print("Error:", error)
else:
    print("Division =", result)

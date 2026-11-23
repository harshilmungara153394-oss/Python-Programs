print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
try:
    number = int(input("Enter a number: "))
    print("Number =", number)
except ValueError:
    print("Invalid input.")
finally:
    print("Finally block executed.")

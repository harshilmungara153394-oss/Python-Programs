print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)
total = sum(int(digit) ** power for digit in digits)
 
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

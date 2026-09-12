#Python Program to Demonstrate Use of Various Arguments Passed to Functions
print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
print("Harshil Mungara")
def student_info(name, enroll, course="M.Sc.(CS&CL)"):
    print("Name:", name)
    print("Enrollment:", enroll)
    print("Course:", course)
student_info("Harshil", 92600565016)
student_info("Vishal", 92600565015, "MBA")

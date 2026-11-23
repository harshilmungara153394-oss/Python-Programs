print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
file = open("sample.txt", "w")
file.write("Hello, this is file handling in Python.")
file.close()
 
file = open("sample.txt", "r")
content = file.read()
print("File Content:", content)
file.close()

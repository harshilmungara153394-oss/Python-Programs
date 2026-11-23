print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
# Write mode
with open("modes.txt", "w") as file:
    file.write("First line\n")
 
# Append mode
with open("modes.txt", "a") as file:
    file.write("Second line\n")
 
# Read mode
with open("modes.txt", "r") as file:
    print(file.read())
 
# Read and write mode
with open("modes.txt", "r+") as file:
    print("File opened in r+ mode.")

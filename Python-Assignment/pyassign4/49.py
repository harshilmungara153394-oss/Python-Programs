print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
text = input("Enter a string: ")
vowels = 0
consonants = 0
 
for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1
 
print("Vowels =", vowels)
print("Consonants =", consonants)

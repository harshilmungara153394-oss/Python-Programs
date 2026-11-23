print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
import whois
 
domain = input("Enter domain name: ")
try:
    info = whois.whois(domain)
    print("Registrar Name:", info.registrar)
except Exception as error:
    print("WHOIS lookup failed:", error)

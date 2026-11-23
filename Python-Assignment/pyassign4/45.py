print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
import whois
 
domain = input("Enter domain name: ")
try:
    info = whois.whois(domain)
    print("Domain Creation Date:", info.creation_date)
except Exception as error:
    print("WHOIS lookup failed:", error)

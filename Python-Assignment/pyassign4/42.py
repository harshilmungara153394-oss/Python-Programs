print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
# Install package: pip install python-whois
import whois
 
domain = input("Enter domain name (e.g. example.com): ")
try:
    result = whois.whois(domain)
    print(result)
except Exception as error:
    print("WHOIS lookup failed:", error)

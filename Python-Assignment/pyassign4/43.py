print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
import whois
 
domain = input("Enter domain name: ")
try:
    info = whois.whois(domain)
    print("Domain:", domain)
    print("Registrar:", info.registrar)
    print("Creation Date:", info.creation_date)
    print("Expiration Date:", info.expiration_date)
    print("Name Servers:", info.name_servers)
except Exception as error:
    print("Unable to retrieve WHOIS information:", error)

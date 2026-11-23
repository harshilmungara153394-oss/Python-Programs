print("M.Sc.(CS&CL) Semester 1")
print("Enrollment No.: 92600565016")
 
import matplotlib.pyplot as plt
 
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 30, 45, 50]
 
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

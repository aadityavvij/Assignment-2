# 2.  Store your name, SID, department name and CGPA into different variables. 
#     With the help of String formatting print the following output: 
#     Hey, ABC Here! 
#     My SID is 2110XXXX 
#     I am from XYZ department and my CGPA is 9.9

name = input("Enter your name\n")
sid = input("Enter your SID\n")
department = input("Enter your department\n")
cgpa = input("Enter your CGPA\n")

print(f"Hey, {name} Here!\nMy SID is {sid}\nI am from {department} department and my CGPA is {cgpa}\n")

# 4.  Write a python program to find the greatest of three numbers entered by the 
#     user.

a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
c = int(input("Enter third number\n"))

if(a>b):
    g1 = a
else:
    g1 = b

if(g1>c):
    print(g1, "is greatest")
else:
    print(c, "is greatest")
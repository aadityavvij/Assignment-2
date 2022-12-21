# 7. Given two numbers A and B. Write a program to count the number
#    of bits needed to be flipped to convert A to B. 

a = int(input("Enter a\n"))
b = int(input("Enter b\n"))

# XOR operator(^) gives 1 for different a and b
# And 0 for same a and b in binary

c = bin(a^b)

print("Number of bits needed to be flipped to convert a to b :", c.count("1"))
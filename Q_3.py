# 3.  For a=56 and b=10 with the help of bitwise operators calculate the following: 
#     a.  a&b 
#     b.  a|b 
#     c.  a^b 
#     d.  Left shift both a and b with 2 bits. 
#     e.  Right shift a with 2 bits and b with 4 bits.

a = 56
b = 10

print(f"a. a&b: {a&b}\n")
print(f"b. a|b: {a|b}\n")
print(f"c. a^b: {a^b}\n")
print(f"d. Left shifting a with 2 bits: {a << 2}")
print(f"   Left shifting b with 2 bits: {b << 2}\n")
print(f"e. Right shifting a with 2 bits: {a >> 2}")
print(f"   Right shifting b with 4 bits: {b >> 4}\n")
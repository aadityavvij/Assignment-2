# 1.  For a given input string “Python is a case sensitive language”. Write python 
#     code for the following: 
#     a.  Find the length of the input string. 
#     b.  Reverse the order of the string in one line code. 
#     c.  Using Slice function store “a case sensitive” in new string. 
#     d.  Replace “a case sensitive” with “object oriented”. 
#     e.  Find index of substring “a” in the given input string. 
#     f. Remove the white spaces from the given input string.

string = "Python is a case sensitive language"
print("\n")

a = len(string)
print(f"a. {a}\n")

b = "Python is a case sensitive language"[::-1]
print(f"b. {b}\n")

c = string[slice(10, 26)]
print(f"c. {c}\n")

d = string.replace("a case sensitive", "object oriented")
print(f"d. {d}\n")

e = string.find("a")
print(f"e. {e}\n")

f = string.strip()
print(f"f. {f}\n")
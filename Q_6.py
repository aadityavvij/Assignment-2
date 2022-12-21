# 6.  For any three lengths, there is a simple test to see if it is possible to form a 
#     triangle. If any of the three lengths is greater than the sum of the other two, 
#     then  you  cannot  form  a  triangle.  Otherwise,  Enter  three  sides  of  a  triangle, 
#     converts them to integers, and to check whether the given input lengths can 
#     form a triangle or not (Print : “Yes” or “No”).

print("\nTHIS IS A PROGRAM TO CHECK WHEATHER SIDES FORM TRIANGLE OR NOT\n")
a = int(input("Enter the first side length\n"))
b = int(input("Enter the second side length\n"))
c = int(input("Enter the third side length\n"))

while (a<b+c & b<a+c & c<a+b):
    print("Yes")
else:
    print("No")
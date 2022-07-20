print("Enter 'a' side of the triangle: ")
a=int(input())
print("Enter 'b' side of the triangle: ")
b=int(input())
print("Enter 'c' side of the triangle: ")
c=int(input())

sides=[a,b,c]
longest_side=(max(sides))

if ((a+b+c)-longest_side)>longest_side:
    print("The triangle is valid")
else:
    print("The entered sides can't create a triangle, the triangle is impossible")

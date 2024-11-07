# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
num1 = int(input("Enter first length: "))
num2 = int(input("Enter second length: "))
num3 = int(input("Enter third length: "))

if num1==num2==num3:
    print("Length is equilateral")
elif num1 == num2 != num3:
    print("Length is isosceles: ")
else:
    print("Length is scalence: ")

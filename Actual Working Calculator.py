#Rajnesh Joshi
print("Welcome To Rajnesh's Calculator Contraption")
print("Enter + For Addition")
print("Enter - For Subtraction")
print("Enter * For Multiplication")
print("Enter / For Division")
print("Enter ** For Exponent")
print("Enter // For Square Root")
print("If you want Square Root simply type 0 for the second number!")
x=input("Enter the first number, Kind Sir:")
y=input("Enter the second number or exponent, Thank You:")
x=float(x)
y=float(y)
z=float(.5)
chooseninput=input("What Do You Choose:(+,-,*,/,**,//: ")
if chooseninput == "+":
    print("The answer is",x+y)
if chooseninput == "-":
    print("The answer is",x-y)
if chooseninput == "*":
    print("The answer is", x*y)
if chooseninput == "/":
    print("The answer is",x/y)
if chooseninput == "**":
    print("The answer is",x**y)
if chooseninput == "//":
    print("The answer is",x**05)
print("Thank You For Using Rajnesh's Calculator Contraption")

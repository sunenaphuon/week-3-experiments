# a) Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    
    
#b) Decimal equivalents of fractions using for loop
print("Decimal equivalents:")
for i in range(2, 11):
    print(f"1/{i} = {1/i}")
        
        
           
# c) Reverse a number
num = int(input("Enter a number to reverse: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print("Reversed number:", reversed_num)


# d) Find biggest among 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is {largest}")


# e) Countdown using while loop
num = int(input("Enter a number to start countdown: "))
while num >= 0:
    print(num)
    num -= 1
print("Countdown complete!")


# a) Sum of two command line arguments
import sys

if len(sys.argv) == 3:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(f"Sum: {num1 + num2}")
    except ValueError:
        print("Please enter valid numbers")
else:
    print("Usage: python program.py <num1> <num2>")
    
    
    # b) Demonstration of various operators
    a = 10
    b = 3

    print("Arithmetic Operators:")
    print(f"Addition: {a + b}")        
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")  
    print(f"Division: {a / b}")        
    print(f"Floor Division: {a // b}") 
    print(f"Modulus: {a % b}")         
    print(f"Exponent: {a ** b}")       

    print("\nComparison Operators:")
    print(f"Equal: {a == b}")          
    print(f"Not Equal: {a != b}")
    print(f"Greater Than: {a > b}")    
    print(f"Less Than: {a < b}")       

    print("\nLogical Operators:")
    x = True
    y = False
    print(f"AND: {x and y}")           
    print(f"OR: {x or y}")             
    print(f"NOT: {not x}")             

    print("\nAssignment Operators:")
    c = 5
    c += 3  
    print(f"+= : {c}")       


# c) Check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote yet.")


# d) Check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")     
         
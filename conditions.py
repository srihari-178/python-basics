#1. positive,negative,zero
num = int(input("Enter a number:" ))
if num > 0: 
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# 2. check if a number is odd or even
num = int(input("Enter a number:"))
if num%2 ==0:
    print("Even")
else:
    print("Odd")

#  #3. largest of two numbers
num_1 = int(input("Enter a num1:"))
num_2 = int(input("Enter a num2:"))
if num_1>num_2:
    print(num_1,"is greater than num_2")
elif num_2>num_1:
    print(num_2,"is greater than num_1")
else:
    print(num_1,"is equal to",num_2)  

# 4) Pass or fail
marks = int(input("enter marks:"))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#5) Grade Calculator

marks = int(input("enter the marks:"))
if marks>=90:
    print("A")
elif marks>=75 and marks <=89:
    print("B")
elif marks>=60 and marks <=74:
    print("C")
elif marks>=40 and marks <=59:
    print("D")
else:
    print("Fail")  

#6) Ask the user to print a  year

year = int(input("Enter a year"))
if year%400 == 0 :
    print("leap year")
elif year%4 == 0 and year%100!=0:
    print("leap year")
else:
    print("not a leap year")

#7) ask the user to print age
age = int(input("enter the age:"))
if age<13:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior Citizen")

#8) Login validation

user_name = str(input("Enter your username:"))
password = str(input("Enter a password:"))
if user_name=="admin" and password=="admin123":
    print("Login successful")
else:
    print("Invalid username or password")

#9) check whether a number is divisible by both 5 and 11

num = int(input("Enter a num:"))
if num%5 == 0 and num%11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

# 10) ask the user for two numbers and operator
num_3 = int (input("Enter a num:"))
num_4 = int(input("Enter a num:"))
operator = str(input("Enter an operator:"))
if operator=="+":
    print(num_3+num_4)
elif operator=="-":
    print(num_3-num_4) 
elif operator=="*":
    print(num_3*num_4)
elif operator=="/":
    if num_4==0:
        print("Cannot divide by zero")
    else:
        print(num_3/num_4)
else:
    print("Invalid operator")









# 24) a program that acts as a simple calculator--

num1 = float(input("Enter number 1:- "))
num2 = float(input("Enter number 2:- "))
operator = input("Enter any one of operator among'+,-,*,/' here:- ")
sum = float(num1 + num2)
diff = float(num1 - num2)
product = float(num1*num2)
quotient = float(num1/num2)

if (operator == "+"):
    print("The sum is:- ",sum)
elif(operator == "-"):
    print("The difference is:- ",diff)
elif(operator == "*"):
    print("The product is:- ",product)
elif(operator == "/"):
    print("The quotient is:- ",quotient)
else:
    print("Invalid operator provided!!")
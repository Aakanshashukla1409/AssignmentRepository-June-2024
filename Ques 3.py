# 3) a python program that calculates the factorial of a given number--

num = int(input("Enter the number: "))
fact = 1
if num==0 or num == 1:
    fact=1
elif num<0:
    print("can't find factorial for negative number")
    fact = 'Inf'
else:
    while(num>0):
        fact = fact*num
        num = num-1
        
print("the factorial of the number is: ",fact)


# 13) a program that asks the user for their birth year and calculates their age

year = int(input("Enter your birth year here:-"))
diff = int(2024-year)

if 2024>year>1000:
    print("Your current age is:- ",diff)
else:
    print("Invalid input provided!!")
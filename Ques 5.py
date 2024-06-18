# 5) a program that takes a string input from the user and writes it to a text file--

string = input("Enter your string here:- ")
samplefile = open('C:/Users/HP/Java/demo.txt','w')
print(string,file = samplefile)

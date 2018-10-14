#Purpose of the program
print("Program to Determine is a given year is a leap year")
year=int(input("Enter yearto be Checked."))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year")
else:
    print("The year isn't a leap year!")
    

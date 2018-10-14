from math import pi
#the purpose of the program
print("the purpose of the program is to test the knowledge of shapes")
#instruction
print("user can only pick one option")
#display instruction
menu=int(input("select any option\n 1)square\n 2)triangle\n 3)rectangle\n 4)circle\n"))
if menu==1:
    print("option 1. square")
    length=int(input("enter the length of a square"))
    area=length*length
    print("area of a square is", area,"cm")
#display option 2
elif menu==2:
    print("option 2. triangle")
    base=int(input("enter the base of a triange"))
    height=int(input("enter the height of a triangle"))
    area=1/2*base*height
    print("area of a square is",area,"cm")
#display option 3
elif menu==3:
    print("option 3. rectangle")
    length=int(input("enter the length of a rectangle"))
    breadth=int(input("enter the breadth of a rectangle"))
    area=length*breadth
    print("the area of a rectangle is",area)
#display option 4
elif menu==4:
    print("option 4. circle")
    radius=int(input("enter the radius of the circle"))
    #pie=22/7
    area=pi*(radius**2)
    print("the area of a circle is",area)
    print(round(area,2))
#else:
    #print("invalid option")
#ask the user to make a choice
#print out the users choice

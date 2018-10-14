#import maths library
import math
#purpose of the program
print("WELCOME TO ALL PURPOSE CALCULATOR")
#programs instructions
print("Select which shape you would want to calculate it value.")
#display shapes
s=int(input("1."+"Rectangle\n2."+"Circle\n3."+"Square\n4."+"Triangle\n5."+"Trapezium\nAns:"))
#use of the ilterations/loops and also to kickoff program
#ilteration for Rectangle
if(s==1):
    print("what do you want to calculate?")
    l=int(input("1."+"AREA\n2."+"PERIMETER\nAns:"))
    if(l==1):
        e=int(input("The length value:"))
        k=int(input("The breadth value:"))
        a=e*k
        print("The Area of such Rectangle:",a)
    elif(l==2):
            e=int(input("The length value:"))
            k=int(input("The breadth value:"))
            p=e+k
            print("The Perimeter of such Rectangle:",p)
    else:
        print("invalid syntax")
    print("Thank you for using all purpose calculator")
#ilteration for Circle
elif(s==2):
    print("What do you want to calculate?")
    j=int(input("1."+"AREA\n2."+"CIRCUMFERENCE\n3."+"RADIUS\n4."+"DIAMETER\nAns:"))
    if(j==1):
        r=int(input("The radius value:"))
        n=math.pi
        a=n*r**2
        print("The Area of such Circle:",a)
    elif(j==2):
        r=int(input("The radius value:"))
        n=math.pi
        c=2*n*r
        print("The Circumference of such Circle:",c)
    elif(j==3):
        i=int(input("1."+"from Area\n2."+"from Circumference\nChoice:"))
        if(i==1):
            a=int(input("The Area of the Circle:"))
            n=math.pi
            s=math.sqrt
            r=s(a/n)
            print("Radius is:",r)
        elif(i==2):
            a=int(input("The Circumference of the Circle:"))
            n=math.pi
            r=a/(2*n)
            print("Radius is:",r)
        else:
            print("invalid syntax")
        print("Thank you for using all purpose calculator")
    elif(j==4):
        i=int(input("1."+"from Area\n2."+"from Circumference\nChoice:"))
        if(i==1):
            a=int(input("The Area of the Circle:"))
            n=math.pi
            s=math.sqrt
            d=2*(s(a/n))
            print("Diameter is:",d)
        elif(i==2):
            a=int(input("The Circumference of the Circle:"))
            n=math.pi
            d=2*(a/(2*n))
            print("Diameter is:",d)
        else:
            print("invalid syntax")
        print("Thank you for using all purpose calculator")
    else:
        print("invalid syntax")
    print("Thank you for using all purpose calculator")
#ilteration for Square
elif(s==3):
    print("what do you want to calculate?")
    l=int(input("1."+"AREA\n2."+"PERIMETER\nAns:"))
    if(l==1):
        y=int(input("The length"))
        a=y**2
        print("The Area of a Square is:",a)
    elif(l==2):
        y=int(input("The length"))
        p=2*y
        print("The Perimeter of a Square is:",p)
    else:
        print("invalid syntax")
    print("Thank you for using all purpose calculator")
#ilteration for Triangle
elif(s==4):
    print("what do you want to calculate?")
    l=int(input("1."+"AREA\n2."+"PERIMETER\nAns:"))
    if(l==1):
        b=int(input("input Base:"))
        h=int(input("input Height:"))
        a=0.5*b*h
        print("The Area of a Triangle is:",a)
    elif(l==2):
        b=int(input("input Base:"))
        h=int(input("input Height:"))
        c=int(input("input slantheight:"))
        u=b+h+c
        print("The Perimeter of a Triangle is:",u)
    else:
        print("invalid syntax")
    print("Thank you for using all purpose calculator")
#ilteration for Trapezium
elif(s==5):
    print("what do you want to calculate?")
    l=int(input("1."+"AREA\n2."+"PERIMETER\nAns:"))
    if(l==1):
        a=int(input("input top length:"))
        h=int(input("input Height:"))
        c=int(input("input Base lenth:"))
        A=(c+a/2)*h
        print("The Area of a Trapezium is:",A)
    elif(l==2):
        a=int(input("input top length:"))
        b=int(input("input slantHeight:"))
        c=int(input("input Base length:"))
        p=a+b+b+c
        print("The Perimeter of a Trapezium is:",p)
    else:
        print("invalid syntax")
    print("Thank you for using all purpose calculator")
else:
    print("invalid syntax")
    print("Thank you for using all purpose calculator")
print("Please kindly give us feedback on things to improve.")
#partial end of program

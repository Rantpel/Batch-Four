a=1000
b=625
while a>b:
    print(a)
    c=a%b
    if b>c:
            temp=b
            a=temp
            b=c
            if(c==0):
                break
                print(c)

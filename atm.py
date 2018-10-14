#purpose of the program
print("WELCOME TO GTBANKS ATM")
#programs instructions
print("Slot in Your Card\n")
a=int(input("Your Pin:\n(1-9)-"))
#conditional statement for first Accont
if(a==123456789):
    print("\nWhat Accont Type:")
    t=input("C."+"Currents\nS."+"Savings\n-")
#conditional statement for Currents Account
    if(t.upper()=="C"):
        print("\nWhat Do YOU want To Perform:")
        w=input("W."+"Withdrawal\nD."+"Deposit\nC."+"Check Balance\nM."+"Make Transfer\nP."+"Pay Bills\n-")
#conditional statement for Withdrawal
        if(w.upper()=="W"):
            print("\nHow much do YOU want to withdraw:")
            m=int(input("\n1."+"#1000.00\n2."+"#5000.00\n3."+"#10000.00\n4."+"#15000.00\n5."+"#20000.00\n6."+"#25000.00\n7."+"#30000.00\n8."+"Others\n-"))
            if(m==8):
                l=int(input("ENTER AMOUNT\n#"))
                if(l>100000):
                    print("INVALID, PLEASE CHECK YOUR VALUES")
                else:
                    print("\nPLEASE WAIT WHILE YOUR TRANSACTION IS PROCESSING....")
                    print("\nPlease Take Your Cash: #",l)
            elif(m==1):
                print("\nPLEASE WAIT WHILE YOUR TRANSACTION IS PROCESSING....")
                print("\nPlease Take Your Cash:","#"+"1000.00")
            elif(m==2):
                print("\nPLEASE WAIT WHILE YOUR TRANSACTION IS PROCESSING....")
                print("\nPlease Take Your Cash:","#"+"5000.00")
            elif(m==3):
                print("\nPLEASE WAIT WHILE YOUR TRANSACTION IS PROCESSING....")
                print("\nPlease Take Your Cash:","#"+"10000.00")
            elif(m==4):
                print("\nPLEASE WAIT WHILE YOUR TRANSACTION IS PROCESSING....")
                print("\nPlease Take Your Cash:","#"+"15000.00")
            elif(m==5):
                print("\nPLEASE WAIT WHILE YOUR TRANSACTION IS PROCESSING....")
                print("\nPlease Take Your Cash:","#"+"20000.00")
            elif(m==6):
                print("\nPLEASE WAIT WHILE YOUR TRANSACTION IS PROCESSING....")
                print("\nPlease Take Your Cash:","#"+"25000.00")
            elif(m==7):
                print("\nPLEASE WAIT WHILE YOUR TRANSACTION IS PROCESSING....")
                print("\nPlease Take Your Cash:","#"+"30000.00")
            else:
                print("invalid input")
            print("Thanks For Banking With Us, God Bless.")
#conditional statement for Deposit
        elif(w.upper()=="D"):
            print("GO TO THE COUNTER")
#conditional statement for checkbalance
        elif(w.upper()=="C"):
            print("Your Account Balance:NGN 900,000,000,000.00")
#conditional statement for make Transfer
        elif(w.upper()=="M"):
            e=str(input("NAME OF THE RECIEVER:"))
            K=int(input("ACCOUNT NUMBER:"))
            Y=float(input("AMOUNT:"))
            print(k,"has been Transfered to",k,"of",e)
#conditional statement for paybills
        elif(w.upper()=="P"):
            print("\nWhat Bill Are You Paying For:")
            p=int(input("1."+"Electricity Bill\n-"))
            if(p==1):
                e=str(input("YOUR NAME:"))
                K=str(input("HOUSE ADDRESS:"))
                r=str(input("STATE:"))
                P=str(input("LOCAL GOVERNMENT:"))
                Y=float(input("AMOUNT:"))
                print("PAYMENT SUCCESSFUL")
            else:
                print("invalid input")
        else:
            print("Invalid Input")
        print("Thank YOU For Banking With Us.")

else:
    print("Invalid Account")

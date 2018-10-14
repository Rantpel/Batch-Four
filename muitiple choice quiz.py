#the purpose of the program
print("the purpose of the program to test the knowledge of student on Economics")
#instruction
print("Answer all question")
print("All question carry equal marks")
question1=input("1. "+"If the demand for a good is inelastic, an increase in its price will cause the total expenditure of the consumers of the good to: \n(a)Increase \n(b)Decrease \n(c)Remain the same \n(d)Become zero\n")
#if the question is correct, display:'Correct' and add 1 to the score
if(question1.lower()=="a"):
   print("correct")
   score=0
   score=score+1
else:
    print("wrong")
    score=-1
question2=input("2. "+"The horizontal demand curve parallel to x-axis implies that the elasticity of demand is: \n(a)Zero \n(b)Infinite \n(c)Equal to one \n(d)Greater than zero but less than infinity\n")
if (question2.lower()=="b"):
    print("correct")
    score=score+1
else:
    print("wrong")
    score=-1
question3=input("3. "+"The supply of a good refers to: \n(a)Stock available for sale \n(b)Total stock in the warehouse \n(c)Actual Production of the good \n(d)Quantity of the good offered for sale at a particular price per unit of time\n")
if (question3.lower()=="d"):
    print("correct")
    score=score+1
else:
    print("wrong")
    score=-1
question4=input("4. "+"In the short run, when the output of a firm increases, its average fixed cost: \n(a)Remains constant \n(b)Decreases \n(c)Increases \n(d)First decreases and then rises\n")
if (question4.lower()=="b"):
    print("correct")
    score=score+1
else:
    print("wrong")
    score=-1
question5=input("5. "+"The cost of one thing in terms of the alternative given up is called: \n(a)Real cost \n(b)Production cost \n(c)Physical cost \n(d)opportunity cost\n")
if (question5.lower()=="d"):
    print("correct")
    score=score+1
else:
    print("wrong")
    score=-1
print("your final answer is",score)
if ("score is 5"):
    print("Good Job")
else:
   print("very poor")

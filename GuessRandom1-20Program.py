import random as ran
num=ran.randint(1,20)
flag=True
guess=0
print("Guess My Number 1-20:", end ="")
while flag==True:
    guess=input()
    if not guess.isdigit():
        print("invalid! Enter only 1-20:", end ="")
        break
    elif int(guess)< num:
        print("Too low, try again:",end ="")
    elif int(guess)> num:
        print("Too high, try again:", end ="")       
    else:
     print("correct... my number is " + guess)
     flag=False
                      
            

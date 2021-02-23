# Akarshana Rajesh
# 2/22/21
# Period 7 CVVA
# Math Game


import random
from time import*



def timer():
    for x in range(1,11):
        sleep(1)
        print(x)

score = 0

def correctAnswer():
    global score
    score = score + 1
    print("Your current score: ",score)
    print()

def wrongAnswer():
    global score
    score = score + 0
    print("Your current score: ",score)
    print()


print()
print("Hi! You will be playing a math game!")

print()
name = str(input("What is your name? "))

star = "\u2b52"
print()
print()
print(star+" Hey",name,", I know you love a challenge, so here you go!!")

print(star+" You’ll be playing a math game. The computer will randomly pick a level"
      " of math for you to do. You will have 3 questions to answer!")
print(star+" If you get more or equal to 1 point, you win! If you don't, try again!")
print()
print()

        
########################################################################################################### 
print()
level_list = ['Easy','Medium','Hard']
random_level = random.choice(level_list)

print(star+" The Great Computer has picked a/an " + random_level +" level for you!")
print()
sleep(4)


if random_level is "Easy":
    print("What is the least common multiple of 6 and 8? ")
    timer()
    answer7 = input("Enter answer: ")
    
    if answer7 == "24" or answer7 == "twenty four" or answer7 == "twenty-four":
        print("You're right! Lets move on!")
        correctAnswer()
        
    else:
        print("Aww, you're wrong. Lets move on!")
        print()
        wrongAnswer()
                
    
    print("2) 888 + 88 + 8 + 8 + 8? ")
    timer()
    answer8 = input("Enter answer: ")
    
    if answer8 == "1000" or answer8 == "thousand" or answer8 == "a thousand":
        print("You're right! Lets move on!")
        correctAnswer()
        
        
    else:
        print("Aww, you're wrong. Lets move on!")
        print()
        wrongAnswer()
    
    print("3) 36, 34, 30, 28, 24, … What number should come next?")
    timer()
    answer9 = input("Enter answer: ")
    
    if answer9 == "22" or answer9 =="twenty-two" or answer9 =="twenty two":
        print("You're right!")
        correctAnswer()
        
    else:
        print("Aww, you're wrong. Nice try though!")
        wrongAnswer()
     
        
###########################################################################################################  
elif random_level is "Medium":
    print('1) A bat and ball cost one dollar and ten cents.')
    print("The bat costs one dollar more than the ball. How much does the ball cost? Enter only amount.")
    print()
    timer()
    answer1 = input("Enter answer: ")
    if answer1 == "five" or answer1 =="5":
        print("You're right! Lets move on!")
        correctAnswer()
        
    else:
        print("Aww, you're wrong. Lets move on!")
        print()
        wrongAnswer()

    
    print('2) What is 6 / 2 (1+2)?')
    timer()
    answer2 = input("Enter answer: ")
    if answer2 == "9" or answer2 =="nine":
        print("You're right! Lets move on!")
        correctAnswer()
        
    else:
        print("Aww, you're wrong. Lets move on!")
        print()
        wrongAnswer()
    
    print('The numbers 2 , 3 , 5 and x have an average equal to 4. What is x?')
    timer()
    answer3 = input("Enter answer: ")
    if answer3 == "six" or answer3 =="6":
        print("You're right!")
        correctAnswer()
        
    else:
        print("Aww, you're wrong. Nice try though!")
        print()
        wrongAnswer()
    
      
########################################################################################################### 
else: ##hard
    print("Is 1000/0 = 0? (true/false)")
    timer()
    answer4 = input("Enter answer: ")
    
    if answer4 == "false" or answer4 == "f" or answer4 == "F" or answer4 == "False":
        print("You're right! Lets move on!")
        correctAnswer()
        
    else:
        print("Aww, you're wrong. Lets move on!")
        print()
        wrongAnswer()
    
    print("The set of ordered pairs {(0,0),(2,0),(3,0),(10,0)} represents a function. True or false?")
    timer()
    answer5 = input("Enter answer: ")
    
    if answer5 == "true" or answer5 =="True" or answer5 =="T" or answer5 =="t":
        print("You're right! Lets move on!")
        correctAnswer()
        
    else:
        print("Aww, you're wrong. Lets move on!")
        print()
        wrongAnswer()
    
    print("Mr. Jones sold two pipes at $1.20 each. Based on the cost, his profit one was 20% and his loss on the other was 20%.\
          On the sale of the pipes, he:")
    print("(a) broke even, (b) lost 4 cents, (c) gained 4 cents, (d) lost 10 cents, (e) gained 10 cents")
    print()
    print("Enter the letter...")
    timer()
    answer6 = input("Enter answer: ")
    
    if answer6 == "d" or answer6 =="D":
        print("You're right!")
        correctAnswer()
        
    else:
        print("Aww, you're wrong. Nice try though!")
        print()
        wrongAnswer()
########################################################################################################### 

print(star+" Overall, you're score is: ", score)

if score >= 1:
    print(name,", you won!")

else:
    print(name,", you lost!")
    
cheer_up = random.randint(0,2)

if cheer_up == "1":
    print("You did very well! Have a nice day!")
else:
    print("You did amazing! Have a nice day!")

        



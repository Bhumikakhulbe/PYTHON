import random #this module is imported to access the randint() function
print("This is a 'NUMBER GUESSING GAME'.\nA secret number will be generated between the range specified by you.\nYou have 6 attempts to guess that number.\nALL THE BEST!")
print("\nPlease select the range of the numbers between which you want to guess to number ")
lower=int(input("Enter the starting number: "))
upper=int(input("Enter the ending number: "))
x=random.randint(lower,upper)  #generates a random number between the given range
for i in range(6): #the loop will run 6 times 
    y=int(input("\nEnter your guess: "))
    if(y>upper or y<lower): #checks if the entered number is either present between the specified range or not
        print("The entered number is out of the given range")
    elif (x<y):
        print("Try again!\nThe secret number is smaller than this number.")
    elif (x>y):
        print("Try again!\nThe secret number is larger than this number.")
    else:
        print("congratulations!\nYou guessed the correct number.")
        break  #the loop will break    
print("\nThe game is over.\nThankyou for playing this game!")



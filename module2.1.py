def collatz(number): #a function named collatz(number) is created
    if number%2==0: #checks if number is even
        return(number//2)
    else: #runs if the number is not even
        return(3*number+1)

number=int(input("Enter an integer: ")) #takes a number as input from user
new=collatz(number) #assign the value of the function to a variable called 'new'
print("The collatz sequence is: ")
while new!=1: #the loop will run until 'new' returns 1
    print(new)
    new=collatz(new) #a different value is assigned to 'new' each time the loop runs
    if new==1: #checks if 'new' equals 1
        print(1)
        break #breaks the loop
    
import random #imports a module named 'random'
for y in range(1000): #loop will run 1000 times
    List=[] #creates an empty list
    countH=0
    countT=0
    streakH=0
    streakT=0
    n=int(input("Enter the number of times you want to toss the coin: ")) #takes input 'n' from user
    for i in range(0,n): #loop will run 'n' times
        x=random.randint(0,1) #generates random integer numbers from 0 to 1
        if x==0:
            List.append('H') #add 'H' in the existing list
        else:
            List.append('T') #add 'T' in the existing list
    print("The list of randomly generated Heads and Tails is: \n",List) #the new list will be displayed
    for j in List: #loop will run for all elements in the list
        if j=='H': 
            countH +=1 #countH will be incremented by 1
            if countH==6:
                streakH +=1 #streakH will be incremented by 1
        else:
            countH=0
    for k in List: #loop will run for all elements in the list
        if k=='T':
            countT +=1 #countT will be incremented by 1
            if countT==6:
                streakT +=1 #streakT will be incremented by 1
        else:
            countT=0
    print("Number of times a streak of six Heads occur is: ",streakH) 
    print("Number of times a streak of six Tails occur is: ",streakT)
    print("The percentage of coin flip containing a streak of six heads in a row is:", (streakH/n)*100)
    print("The percentage of coin flip containing a streak of six tails in a row is:", (streakT/n)*100)

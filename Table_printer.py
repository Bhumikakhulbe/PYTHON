from tabulate import tabulate #tabulate module is imported from tabulate library
def printTable(): #function printTable is created
    #input validation
    while True:
        try:
            n=int(input("Enter the number of lists you want in your list: "))
        except ValueError:
            print("Enter an integer value")
            continue #moves to the next iteration
        try:
            l=int(input("Enter the length of each list: "))
        except ValueError:
            print("Enter an integer value")
            continue 
        break #breaks the statement
    List1=[] #empty list is created
    for i in range(1,n+1): 
        List2=[] #empty list is created
        print("Enter the string values in List",i,":")
        for j in range(l): #loop will run till the entered length of list
            val=str(input())
            List2.append(val) 
        List1.append(List2) #list is appended
    print(tabulate(List1,tablefmt="grid", stralign="right")) #A table is created with right justification
printTable() #function is called

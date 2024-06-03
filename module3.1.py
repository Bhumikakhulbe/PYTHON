def displayInventory(): #A function is defined
    #input validation
    while True: #runs till the loop breaks
        try: 
            n=int(input("Enter the number of items you want in your inventory: "))
        except ValueError:
            print("Please enter a numeric value")
            continue 
        break #breaks the loop
    Dict={} #An empty dictionary is created
    total=0 #initilising variable
    print("Create The Inventory:")
    for i in range(n):
        #input validation
        while True:
            try:
                key=str(input("Enter the item: "))
            except ValueError:
                print("Please enter a string value")
                continue #moves to the next iteration
            try:
                value=int(input("Enter the value: "))
            except ValueError:
                print("Please enter an integer value")
                continue
            break
        Dict[key]=value #add items in the dictionary
    print("Inventory:")
    for key , value in Dict.items(): #loop will run for all items in the dictionary
        print(value, key) #the keys and value will be printed
        total = total+ value #calculate the total number of items
    print("Total number of items:",total)
displayInventory() #calling the function

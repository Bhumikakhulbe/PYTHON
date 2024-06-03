def addToInventory(Inventory, addedItems): #a function that takes two parameters
    count=0 #Initialising the variable
    for j in addedItems: #loop will run for all items in the list
        if j in Inventory:
            Inventory[j] += 1
        else:
            Inventory[j] = 1
    print("\n\nUpdated Inventory:")
    for key, value in Inventory.items(): #loop will run for all items in the dictionary
        print(value, key)
        count=count+value #counts the total number of items 
    print("Total number of Items: ", count)
        
Inventory={'arrow':12, 'gold chain':42, 'rope':1, 'torch':6, 'dagger':1} #pre-existing dictionary
count1=0 #Initialising the variable
print("\nInventory:")
for key, value in Inventory.items(): #loop will run for all items in the dictionary
        print(value, key)
        count1= count1+ value #counts the total number of items 
print("Total number of Items: ", count1)
addedItems=[] #empty list is created
#input validation
while True:
    try:
        n=int(input("\n\nEnter the number of new items you want to add: "))
    except ValueError:
        print("Enter an Integer value")
        continue
    break
for i in range(n):
    #input validation
    while True:
        try:
            a=str(input("Enter Item: "))
            addedItems.append(a)
        except ValueError:
            print("Enter a string value")
            continue
        break
addToInventory(Inventory, addedItems) #calling the function

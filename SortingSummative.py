#######################################
#Kale Berger
#Start date: October 12, 2018
#End Date:
#Sorting Summative
#######################################

def bubbleSort(GroceryList): #funtion to sort the list alphabetically
    for passnum in range(len(GroceryList)-1,0,-1):
        for i in range (passnum):
            if GroceryList[i]>GroceryList[i+1]:
                temp = GroceryList[i]
                GroceryList[i] = GroceryList[i+1]
                GroceryList[i+1] = temp
                
GroceryList = ["milk"]
#This will be the dictionary that will use user input to add items to this list
#will be sorted by food group using quick sort

def addtolist():#function to add items to the list
    print("This is your current grocery list:", GroceryList)
    additem = input("Do you want to add an item?: ")
    while additem == ("yes"):
        item = input("Item: ")
        GroceryList.append(item)
        additem = input("Do you want to add another?: ")
    else:
        print("Your full list is:", GroceryList)
        
        
def removefromlist(): #Function to remove items from the list  
    print("You have went shopping and bought a couple items from your list.")
    keepremoving =input("do you want to remove an item?: ")
    while keepremoving == ("yes"):
        removeitem = input("list 1(one) item at a time. You bought: ")
        GroceryList.remove(removeitem)
        keepremoving = input("Do you want to remove another item?: ")
    else:
        print ("On your grocery list, remains these items:", GroceryList)

def changeitemonlist(): #Function to edit errors in the list
    print ("You realize that you wrote down a wrong item on your list *gasp*!")
    changeitem = input("Do you want to change an item?: ")
    while changeitem == ("yes"):
        change = input("What item do you want to change?: ")
        GroceryList.remove(change)
        change = input("What would you like to change it to?: ")
        GroceryList.append(change)
        changeitem = input ("Change another item?: ")
    else:
        print(GroceryList)

addtolist()
removefromlist()
changeitemonlist()
bubbleSort(GroceryList)#sorts the list
print("This is your current alphabetically sorted grocery list:", GroceryList)#prints the alphabetically sorted final list
    


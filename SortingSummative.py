#######################################
#Kale Berger
#Start date: October 12, 2018
#End Date:
#Sorting Summative
#######################################
def bubbleSort(GroceryList):
    for passnum in range(len(GroceryList)-1,0,-1):
        for i in range (passnum):
            if GroceryList[i]>GroceryList[i+1]:
                temp = GroceryList[i]
                GroceryList[i] = GroceryList[i+1]
                GroceryList[i+1] = temp
                
GroceryList = ["milk"]
#This will be the dictionary that will use user input to add items to this list
#will be sorted by food group using quick sort


print("This is your current grocery list:", GroceryList)
additem = input("Do you want to add an item?: ")
while additem == ("yes"):
    item = input("Item: ")
    GroceryList.append(item)
    additem = input("Do you want to add another?: ")
else:
    print("Your full list is:", GroceryList)
    print("Now your list will be sorted alphabetically")
    bubbleSort(GroceryList)
    print(GroceryList)

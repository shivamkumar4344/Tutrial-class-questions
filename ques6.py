# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1, 2, 5, 2, 5, 1, 3, 7, 9]
# Expected Result : [1,2,5,3,7,9] 

def getUniqueElements(numList):
    unique = []
    for i in numList:
        if i not in unique:
            unique.append(i)
    
    print(unique)
    
numbersList = [1, 2, 5, 2, 5, 1, 3, 7, 9]

getUniqueElements(numbersList)


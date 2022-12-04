# Write a Python function to multiply all the numbers in a list
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

mul = 1
list2 = [8,2,3,-1,7]
for i in range(0,len(list2)):
    mul = mul*list2[i]
print("Product of total elements in list2=",mul)
#2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
total = 0
list1 = [8,2,3,0,7]
for ele in range(0,len(list1)):
    total = total+list1[ele]

print("Sum of total elements in a list1="total)
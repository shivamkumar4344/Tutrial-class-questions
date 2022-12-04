# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8] 

list3 = [1,2,3,4,5,6,7,8,9]
for num in list3:
    if num%2==0:
        print(list(num),end=",")
    

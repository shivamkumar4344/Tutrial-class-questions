# Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

n = int(input("Enter the number:- "))
for i in range(n+1,0,-1):
    for j in range(1,i):
        print(j,end= " ")
    print(" ")
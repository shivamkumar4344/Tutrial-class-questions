# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

sum = 0
n = int(input("Enter the number:- "))
for i in range(0,n+1):
    sum=sum+i
print("Sum of first n natural numbers is ",sum)
# Calculate the cube of all numbers from 1 to a given number
# Example - input_number = 6
# Output
# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216

n = int(input("Enter the number: "))
i = 1
for i in range(1,n+1):
    n = i
    i=i**3
    print(f"current number is : {n} and the cube is {i}")
    
    
    



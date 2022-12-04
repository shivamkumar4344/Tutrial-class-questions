#1. Write a Python function to find the Max of three numbers.
def max_of_three(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z

x = int(input("Enter the value of x="))
y = int(input("Enter the value of y="))
z = int(input("Enter the value of z="))
print(max_of_three(x,y,z))
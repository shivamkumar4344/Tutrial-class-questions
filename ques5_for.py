# Write a program to display all prime numbers within a range, take start range and end range from the user
start=int(input("Enter the starting range: "))
end=int(input("Enter the ending range: "))
x=[]
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
               break
        else:
            x.append(i)
#print(x)
y=[]
for k in x:
    if k not in y:
        y.append(k)
    else:
        continue
print(y)

                    

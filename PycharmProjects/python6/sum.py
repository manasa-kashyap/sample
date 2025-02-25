n=int(input("enter a number (N)to sum numbers from 1 to N:"))
total=0
for i in range(1,n+1):
    total +=i
print(f"the sum of numbers from 1 to {n} is {total}")
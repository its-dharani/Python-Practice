n=int(input())
factors=[]
for i in range (1,n):
    if n % i==0:
        factors.append(i)
s=sum(factors)
if s==n:
    print("Perfect Number")
else:
    print("Not a perfect number")
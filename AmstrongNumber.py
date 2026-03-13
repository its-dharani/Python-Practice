n=int(input())
digits=list(map(int,str(n)))
pow=len(digits)
sum=0
for i in digits:
    sum+=i**pow
if sum==n:
    print("Amstrong Number")
else:
    print("Not Amstrong Number")
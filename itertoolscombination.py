from itertools import combinations
s,k=input().split()
k=int(k)
s=sorted(s)
for i in range (k,k+1):
    for char in combinations(s,k):
        print(''.join(char))
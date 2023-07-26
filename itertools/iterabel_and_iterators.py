from itertools import combinations
N=int(input())
lst=list(input().split())
L=int(input())

combo=list(combinations(lst,L))
sum=0
for i in (combo):
    if 'a' in i :
        sum+=1
print(float(sum/len(combo)))
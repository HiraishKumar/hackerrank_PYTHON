x=input()
set1=set(map(int,input().split()))
y=input()
set2=set(map(int,input().split()))
a=set1.union(set2)
b=set1.intersection(set2)

for i in b:
    a.remove(i)
    
for i in (sorted(list(a))) :
    print(i)
    
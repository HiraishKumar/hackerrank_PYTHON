from collections import Counter 
n,m=input().split()

b=Counter(list(map(int,input().split())))

c=set(map(int,input().split()))

d=set(map(int,input().split()))
happy=0
for i in c:
    happy+=b[i] 
for j in d:
    happy-=b[j] 

    
print(happy)


    
# With sequence of items  
# a=(Counter(['B','B','A','B','C','A','B',
#                'B','A','C']))
# print(a['B'])

    
from itertools import combinations as p

str1,int1=input().split()
for i in range (1,int(int1)+1):
    for j in (p(sorted(str1),i)):  
        print(''.join(j))

from itertools import permutations

a=input().split()
lst=list(a)

for i in sorted(permutations(lst[0],int(lst[1]))):
    print(''.join(i))


    

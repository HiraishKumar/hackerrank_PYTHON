from collections import defaultdict as dd 
n,m=map(int,input().split())        #inital parameters for how many elements will the dd have (n) 
                                    #and how many have to be later checked through dd (m)
A=[]                                #initializing list
B=dd(list)                          #initializing dd

for _ in range(n):                  #filling the list to use enumerate 
    A.append(input())

for index, key in enumerate(A):     #key:value pair of element(key) and its postion(value) 
    B[key].append(index+1)
# print(dict(B))
for _ in range(m):
    # try:                            #combining the value of all the keys to be printed with a ' ' in between
    #     print(' '.join(str(index) for index in B.get(input())))
    # except:
    #     print(-1)                   #if one of the test elements not part of the dd print(-1)
    
    
    print(' '.join(str(index) for index in B.get(input(),[-1])))
    
    #Vs
    
    try: 
        print(' '.join(str(index) for index in B.get(input())))
    except:
        print(-1)
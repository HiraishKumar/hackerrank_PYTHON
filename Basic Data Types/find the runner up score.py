if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=[]
    for j in arr:
        l.append(j)
    
    l.sort()
           
    for i in l:
        if (i==max(l)):
            l[l.index(i)]=-99
        else:
            pass
    
    print (max(l))
    
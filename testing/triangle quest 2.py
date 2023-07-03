a=5


for i in range(1,a):
    for i in range (0,a):
        lst1=[]
        if 0<i<a:
            lst1.append(i)
        else:
            pass
        lst1=map(str,lst1)
        lst2=[]
        lst2.append(a-i)
        lst2=map(str,lst2)
        x=''.join(lst1)
        y=''.join(lst2)
        print(x+y)



string=input()

lo,up,ev,od=[],[],[],[]
for i in string:   
    if i.isdigit():
        if int(i)%2==0:
            ev.append(i)
        else:
            od.append(i)
    elif i.isupper():
        up.append(i)
    elif i.islower():
        lo.append(i)
lo,up,ev,od=sorted(lo), sorted(up), sorted(ev), sorted(od)     
print(''.join(lo)+''.join(up)+''.join(od)+''.join(ev))
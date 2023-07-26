N=int(input())
stri=input()
try:
    lst=list(map(int,input().split()))
except:
    lst=[int(stri)]
if all( i>0 for i in lst):
    for i in lst:
        if str(i)==str(i)[::-1]:
            print('True')
        else:
            print('False')
else:
    print('False')
          


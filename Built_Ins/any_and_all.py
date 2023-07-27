N=int(input())
stri=input()
try:
    lst=list(map(int,stri.split()))
except:
    lst=[int(stri)]
if all( i>0 for i in lst):
    if any(str(i)==str(i)[::-1] for i in lst):
        print('True')
    else:
        print('False')
else:
    print('False')
          
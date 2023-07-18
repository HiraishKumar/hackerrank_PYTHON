from itertools import groupby
from time import time
string=input()

start=time()

lst=[int(string[i]) for i in range(len(string))]
print(*[tuple((len(list(val)),key)) for key,val in groupby(lst,key=lambda x:x)])

finish=time()
print('Eexecution time:',round(finish-start,8),'Seconds')



# lst=[]
# for i in range(len(string)):
#     if string[i] not in lst:
#         lst.append([0,int(string[i])])
# print(lst)
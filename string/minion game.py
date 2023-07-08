
stuart=0 #if vowel
kevin=0 # if conso
string='ANANAS'
vowel='AEIOU'
lst=[]
for i in range(0,len(string)):
    temp=''
    for j in range (i,len(string)):
        temp+=string[j]
        lst.append(temp)
        
# for i in lst:
#     print(i)
for i in lst:
    if i[0] in vowel:
        stuart+=1
    else:
        kevin+=1

if kevin > stuart:
    print('Kevin',str(kevin))
else:
    print('Stuart',str(stuart))
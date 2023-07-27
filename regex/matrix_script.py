import re
n,m=map(int,input().split())
matrix = []
lst = []
for i in range(n):
    matrix.append([x for x in input()])
    
for i in range(m):
    for j in range(n):
        lst.append(matrix[j][i])
path = re.compile(r'\b[ !@#$%&]+\b', re.M)
k = re.sub(path, ' ',''.join(lst))
print(k)

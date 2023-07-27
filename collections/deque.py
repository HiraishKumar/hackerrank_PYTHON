from collections import deque
d=deque()
for i in range(int(input())):
    com=input().split()
    if com[0]=='append':
        d.append(com[1])
    elif com[0]=='pop':
        d.pop()
    elif com[0]=='popleft':
        d.popleft()
    elif com[0]=='appendleft':
        d.appendleft(com[1])
print(*d)

'''
6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''
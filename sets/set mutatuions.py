a=int(input())
Mset=set(map(int,input().split()))
for _ in range (int(input())):
    k=input().split()
    
    if k[0]=='intersection_update':
        Mset.intersection_update(set(map(int,input().split())))
    elif k[0]=='update':
        Mset.update(set(map(int,input().split())))
    elif k[0]=='symmetric_difference_update':
        Mset.symmetric_difference_update(set(map(int,input().split())))
    elif k[0]=='difference_update':
        Mset.difference_update(set(map(int,input().split())))
        
print(sum(Mset))


'''
We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
'''
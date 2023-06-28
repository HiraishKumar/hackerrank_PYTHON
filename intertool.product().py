from itertools import product 
#product gives the cartesian products of the the 
#elements of the 2 lists that are given as arguments 
#cartesian product: product([a,b],[1,2])==[(a,1),(a,2),(b,1),(b,2)] 

a=input().split()
b=input().split()
# the function of .split() here is spliting the string (of input) 
# which can (in the nesxt line) be turned into a list
lst1=list(a)
lst1=(map(int,lst1))
#the map here turns every element of the list (which is a string) into a integer

lst2=list(b)
lst2=(map(int,lst2))

lst3=list(product(lst1,lst2))
print(*lst3)
#the '*' before the lst is there so that each element of the list can be presented with one space in between 

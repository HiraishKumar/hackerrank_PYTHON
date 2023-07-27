N=int(input())
Shoe_size=list(map(int,input().split()))
customers=int(input())
sum=0
for i in range (customers):
    size,price=map(int,input().split())
    if size in Shoe_size:
        sum+=price
        Shoe_size.remove(size)
    else:
        pass
print(sum)

'''
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
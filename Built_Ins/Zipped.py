N,M = map(int, input().split())
lst = [map(float, input().split()) for i in range(M)]
for i in zip(*lst):
    print(sum(i)/M)
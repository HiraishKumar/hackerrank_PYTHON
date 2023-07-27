from collections import Counter
integer1 = int(input())
words = [input() for _ in range(integer1)]
con=Counter(words)
print(len(con.keys()))
print(*[con[i] for i in con])
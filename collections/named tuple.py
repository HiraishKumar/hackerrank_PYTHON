from collections import *
N = int(input())
cri = input().split()
Student = namedtuple('Student',cri)

sum = 0
for i in range(N):
    st = Student(*(input().split()))
    sum += int(st.MARKS)
    
print(f"{sum/N:.2f}")
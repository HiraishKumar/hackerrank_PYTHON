for i in range(int(input())):
    a=int(input())
    set1=set(map(int,input().split()))
    b=int(input())
    set2=set(map(int,input().split()))
    if set1.issubset(set2):
        print('True')
    else:
        print('False')
        
'''Input Format

The first line will contain the number of test cases,T .
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A .
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.


Output Format

Output True or False for each test case on separate lines.

Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False'''
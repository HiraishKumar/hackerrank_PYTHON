'''
Task

You are given a square matrix A with dimensions NXN. Your task is
to find the determinant. Note: Round the answer to 2 places 
after the decimal.

Input Format

The first line contains the integer N .
The next N lines contains the N space separated elements of array .

Output Format

Print the determinant of A.

Sample Input

2
1.1 1.1
1.1 1.1
Sample Output

0.0
'''
import numpy as np
print(round(np.linalg.det(np.array([list(map(float,input().split())) for i in range(int(input()))])),3))


 
    

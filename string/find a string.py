def count_substring(string, sub_string):
        
    sub=[]
    for i in range (len(sub_string)):
        sub.append(sub_string[i])
    
    lst1=[]
    for j in range (len(string)-len(sub_string)+1):  
        lst2=[]
        for k in range(len(sub_string)):
            lst2.append(string[j+k])
        lst1.append(lst2)
        
    return(lst1.count(sub))
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2'''
if __name__ == '__main__':
    s = input()

    print(True in list(map(lambda n:n.isalnum(),s)))
    print(True in list(map(lambda n:n.isalpha(),s)))
    print(True in list(map(lambda n:n.isdigit(),s)))
    print(True in list(map(lambda n:n.islower(),s)))
    print(True in list(map(lambda n:n.isupper(),s)))


'''Task

You are given a string s .
Your task is to find out if the string contains: alphanumeric characters, alphabetical characters,
digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
In the second line, print True if s has any alphabetical characters. Otherwise, print False.
In the third line, print True if s has any digits. Otherwise, print False.
In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True'''
def print_rangoli(size):
    # your code goes here
    alphbets = "abcdefghijklmnopqrstuvwxyz"
    # get char from alphabets, "-char-", next this in center and fill
    total_size = ((4*size)-3)
    for i in range(1, size+1):
        # Form alphabets
        alpha_string = ""
        for j in range(i):
            letter = alphbets[size-i+j]
            alpha_string = alpha_string.center((2*j+1), letter)
        alpha_string_hiphen = "-".join(alpha_string)
        print(alpha_string_hiphen.center(total_size, "-"))                 
    for i in range(size-1, 0, -1):        
        alpha_string = ""
        for j in range(i):                
            letter = alphbets[size-i+j]
            alpha_string = alpha_string.center((2*j+1), letter)
        alpha_string_hiphen = "-".join(alpha_string)
        print(alpha_string_hiphen.center(total_size, "-"))

'''
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

Function Description

Complete the rangoli function in the editor below.

rangoli has the following parameters:

int size: the size of the rangoli
Returns

string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
Input Format

Only one line of input containing size, the size of the rangoli.

Constraints


Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------'''
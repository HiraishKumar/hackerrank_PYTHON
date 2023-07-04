def wrap(string, max_width):
    
    convert = list(string)
    
    lines = []
    line = ""
    
    for i in convert:
        if len(line) < max_width:
            line += i
            
        else:
            lines.append(line)
            line = i
            
    lines.append(line)
    
    return "\n".join(lines)


'''Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''
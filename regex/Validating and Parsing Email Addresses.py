import email.utils
import re
for i in range(int(input())):
    name, emil = email.utils.parseaddr(input())
    if (bool(re.match(r"^[a-z][a-z0-9_.-]+@[a-z]+\.[a-z]{1,3}$", emil))):
        print(email.utils.formataddr((name, emil)))
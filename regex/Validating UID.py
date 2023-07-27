import re

pattern = r'^(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?!.*(.).*\1)[a-zA-Z0-9]{10}$'

print(*['Valid' if bool(re.match(pattern, input()))
      else 'Invalid' for _ in range(int(input()))], sep='\n')
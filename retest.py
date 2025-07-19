import re

str1="This is python"
m=re.search(r'python',str1)
print(m)
print(m.group(0))

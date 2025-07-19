import re

str1="ab abb abbb abbbb acb a"
list1=re.findall(r'ab*',str1)
print(list1)

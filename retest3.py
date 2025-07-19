import re

str1="python java\noracle\tmysql"
list1=re.findall(r'\s',str1)
print(list1)
a=re.split(r'\s',str1)
print(a)

import re
name=input("name:")
m=re.fullmatch(r'^[A-Z]{2,10}\s{1}[A-Z]{2-10}$',name)
if m!=None:
    print(f'{name} is valid')
else:
    print(f'{name} is invalid')

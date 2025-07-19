import re

email=input("Email-id:")
m=re.fullmatch(r'\w{1,15}@\w{1,15}\.\w{2,3}',eamil)
if m!=None:
    print(f'{email} is valid')

else:
    print(f'{email}is invalid')

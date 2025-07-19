import re

ipadd=input("IPAddress:")
m=re.fullmatch(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ipadd)
if m!=None:
    print("valid ip-address")
else:
    print("Invalid ip-address")

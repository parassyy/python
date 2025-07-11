password=input("enter the password")
ac=0
dc=0
sc=0
for i in password:
    if i.isalpha():
        ac+=1
    elif i.isdigit():
        dc+=1
    else:
        sc+=1
print(ac)
print(dc)
print(sc)
if ac>=4 and dc>=2 and sc>=2:
    print("valid")
else:
    print("in valid")

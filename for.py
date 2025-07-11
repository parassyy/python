str=input("enter the any string")
ac=0
dc=0
sc=0
for ch in str:
    if ch>='a' and ch<'z' or ch>='A' and ch<='Z':
        ac+=1
    elif ch>='0' and ch<='9':
        dc+=1
    else:
        sc+=1

print("count of digit:",dc)
print("count of alpabet:",ac)
print("count of splch:",sc)

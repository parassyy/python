str1=input("enter any string:")
str2=''
for ch in str1:
    if ch>='A' and ch<='Z':
        str2=str2+chr(ord(ch)+32)
    else:
        str2=str2+ch
print(f'{str1}-->{str2}')

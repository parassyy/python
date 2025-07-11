num=[10,20,30,40,50,60,70]
largest=num[0]
sec_largest=num[0]
for i in range(len(num)):
    if num[i]>largest:
        largest=num[i]
for i in range(len(num)):
    if num[i]>sec_largest and num[i]!=largest:
        sec_largest=num[i]

print(sec_largest)
        
            

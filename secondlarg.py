num=[78,45,76,90,23,37,84]
largest=num[0]
second_largest=num[0]
for i in range(len(num)):
    if num[i]>largest:
        largest=num[i]

for i in range(len(num)):
    if num[i]>second_largest and num[i]!=largest:
        second_largest=num[i]


        
print(second_largest)

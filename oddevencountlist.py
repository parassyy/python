a=[10,45,87,52,32,44,65,66,98,21,32,45,64,88,55,99,90,22,44,11]
even_count=0
odd_count=0
for i in range(len(a)):
    if a[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
print(a)
print("even_c:",even_count)
print("odd_c:",odd_count)
        

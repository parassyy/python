a1=[10,20,20,30,40,50,50,60,70,70]
dubli=[]
for i in a1:
    if a1.count(i)>1 and i not in dubli:
        dubli.append(i)
print("dublicate item form list:",dubli)

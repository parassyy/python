def sum_val(*values):
    s=0
    for value in values:
        s=s+value
    return s

res1=sum_val(10,20,30,40,50)
print(res1)
res2=sum_val()
print(res2)

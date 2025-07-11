t=(3,7,1,18,9)
k=2
st=tuple(sorted(t))
print(t)
print(st)
min_max=st[:k]+st[-k:]
print(min_max)

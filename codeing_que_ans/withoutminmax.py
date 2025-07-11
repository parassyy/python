#Find the largest and smallest number in a list without using min() or max()

num=[32,12,45,65,98,78,32]
nmax=num[0]
nmin=num[0]
for i in num:
    if i>nmax:
        nmax=i
    if i<nmin:
        nmin=i
print("smallest no. is:",nmin)
print("largest no. is:",nmax
